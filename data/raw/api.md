# NovaSuite API Reference

## Overview

The NovaSuite REST API allows developers to programmatically access and manage tickets, contacts, knowledge base articles, and agents. The base URL for all API requests is https://api.novasuite.io/v1. All responses are returned in JSON format. The current stable version is v1.

API access availability depends on your plan. Read-only access is available on the Growth plan. Full read and write access is available on Business and Enterprise plans. Webhooks and outbound integrations are available on Business and Enterprise plans only.

## Authentication

All API requests must include a valid API key in the Authorization header using the Bearer token format. API keys can be generated from the Settings section of your NovaSuite dashboard under API, then Generate Key. Each key can be scoped to specific permissions such as read-only, read-write, or admin-level access. Keys can be individually labeled and revoked at any time.

You should never expose API keys in client-side code or commit them to version control. Store keys in environment variables and rotate them regularly.

## Rate Limits

The Growth plan allows 100 API requests per minute. The Business plan allows 500 requests per minute. Enterprise customers can negotiate custom limits up to 5000 requests per minute. Rate limit information is returned in the headers of every API response, including the current limit, remaining requests, and the timestamp when the limit resets. When the rate limit is exceeded, the API returns a 429 Too Many Requests response with a retry_after value indicating how many seconds to wait.

## Tickets

The tickets endpoint allows you to list, create, update, and delete support tickets. To list all tickets, send a GET request to /tickets. You can filter results by status, priority, assigned agent, and date range. Results are paginated and return 25 tickets per page by default, with a maximum of 100 per page.

To create a ticket, send a POST request to /tickets with the subject, description, priority, channel, and requester details in the request body. Custom fields can be included to store additional metadata such as account ID or region. The API returns the created ticket object including its assigned ID and initial status.

To update a ticket, send a PATCH request to /tickets followed by the ticket ID. Only the fields included in the request body will be updated. Updatable fields include status, priority, assigned agent, tags, and custom fields.

To add a reply to a ticket, send a POST request to /tickets followed by the ticket ID and then /replies. The reply body must specify whether the message is public, meaning it is visible to the customer, or internal, meaning it is an agent-only note. To permanently delete a ticket, send a DELETE request to /tickets followed by the ticket ID. This action is irreversible and requires an admin-scoped API key.

## Contacts

The contacts endpoint allows you to list and create customer contact records. To list all contacts, send a GET request to /contacts. You can filter by email address, name, company, and creation date range. To create a contact, send a POST request to /contacts with the contact's name, email address, phone number, company, and any custom fields you want to store.

## Knowledge Base Articles

The articles endpoint allows you to list, retrieve, create, and update knowledge base articles. To list all articles, send a GET request to /kb/articles. You can filter by category, publication status, and language. To retrieve a single article with its full content and metadata, send a GET request to /kb/articles followed by the article ID.

To create an article, send a POST request to /kb/articles with the title, HTML body content, category ID, publication status, language code, and tags. To update an existing article, send a PATCH request to /kb/articles followed by the article ID. Each update automatically creates a version snapshot that can be used to roll back changes.

## Agents

The agents endpoint allows you to list and add agent accounts. To list all agents, send a GET request to /agents. The response includes each agent's role, current status, team assignments, and ticket count. To create a new agent, send a POST request to /agents with the agent's name, email address, role, and team assignments. An invitation email is automatically sent to the provided email address. Available roles are admin, manager, agent, and viewer.

## Webhooks

Webhooks are available on Business and Enterprise plans. They allow NovaSuite to send real-time event notifications to an external URL whenever something happens in your workspace. Supported events include a new ticket being received, ticket fields being changed, a ticket being resolved, a ticket being deleted, a customer submitting a CSAT rating, a knowledge base article being published, and a new agent being added.

Each webhook payload includes the event name, a timestamp, your workspace ID, and a data object containing the relevant details for that event. For security, each request includes an HMAC-SHA256 signature in the X-NovaSuite-Signature header. You should verify this signature on your server before processing the payload to ensure the request genuinely came from NovaSuite.

## Error Handling

The NovaSuite API uses standard HTTP status codes to indicate the result of each request. A 200 response means the request was successful. A 201 response means a new resource was created successfully. A 400 response means the request contained invalid parameters. A 401 response means the API key is missing or invalid. A 403 response means the API key does not have permission to perform the requested action. A 404 response means the requested resource does not exist. A 422 response means the request was well-formed but failed validation. A 429 response means the rate limit has been exceeded. A 500 response means an unexpected error occurred on the server side.

All error responses include an error code, a human-readable message, and where applicable the specific field that caused the validation failure.

## Pagination

All list endpoints return paginated results. Use the page and per_page query parameters to navigate through results. Each response includes a meta object with the total record count, the current page number, the number of results per page, and the total number of pages available.

## API Changelog

In January 2025, version 1.3.0 was released. This version added custom fields support for tickets and contacts, introduced the csat.submitted webhook event, and improved error messages with field-level detail. In September 2024, version 1.2.0 was released, adding HMAC signature verification for webhooks, knowledge base article versioning endpoints, and a requirement that ticket deletion use an admin-scoped key. In May 2024, version 1.1.0 was released, adding rate limit headers to all responses, the agents list endpoint, and expanded filter options on the tickets list endpoint.
