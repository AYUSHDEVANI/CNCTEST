# NovaSuite Frequently Asked Questions

## General

### What is NovaSuite

NovaSuite is an all-in-one SaaS platform that combines customer support ticketing, a knowledge base, team collaboration, workflow automation, and analytics into a single dashboard. It is designed for customer support teams, IT helpdesks, and operations teams at companies of any size.

### Is there a free plan

NovaSuite does not offer a permanent free plan. However, all new users get a 14-day free trial on the Growth or Business plan with no credit card required.

### What happens when the free trial ends

When your 14-day free trial ends, your account is automatically placed in read-only mode. You will not lose any of your data, including tickets, articles, and configurations. You can upgrade to a paid plan at any time to restore full access.

### Does NovaSuite work in multiple languages

Yes. The NovaSuite interface supports 28 languages. The knowledge base also supports multi-language content, so you can publish articles in different languages for different audience segments. Language detection can be configured based on the user's browser locale or set manually.

### What kind of companies use NovaSuite

NovaSuite is used by freelancers, small businesses, mid-market companies, and large enterprises. Common use cases include customer support teams managing inbound requests, IT helpdesks handling internal employee tickets, and operations teams automating recurring business processes.

## Billing and Payments

### Can I change my plan at any time

Yes. You can upgrade at any time and the change takes effect immediately with prorated billing. Downgrades take effect at the start of your next billing cycle.

### Is annual billing cheaper than monthly billing

Yes. Annual billing offers a 20 percent discount compared to monthly billing. For example, the Growth plan costs 79 dollars per month on a monthly basis but only about 63.20 dollars per month when billed annually.

### Do you offer refunds

Monthly plan customers cannot receive a refund for the current billing period but can cancel before the next billing cycle. Annual plan customers can request a refund within the first 30 days of the term. After 30 days, no refunds are issued but the account stays active until the term ends.

### Will prices increase after I subscribe

NovaSuite guarantees price lock-in for 12 months from the date of your subscription. If prices change after that period, you will receive at least 30 days of advance notice before the new pricing takes effect on your account.

### How are payments processed

All card payments are processed securely through Stripe. NovaSuite accepts Visa, Mastercard, American Express, and PayPal. Enterprise customers can pay via wire transfer or invoice. NovaSuite does not store your card details directly.

## Features

### How does AI-assisted ticket routing work

When a new ticket arrives, NovaSuite analyzes the subject line, message body, and metadata using a trained classification model. Based on this analysis, it automatically assigns the ticket to the most relevant team or agent and applies appropriate tags and priority levels. This feature is available on the Business plan and above.

### Can I remove NovaSuite branding from the chat widget

Yes. Branding can be removed on the Growth plan and above. Full white-labeling including custom colors, logo, and domain is available on the Business and Enterprise plans.

### Does NovaSuite integrate with Slack

Yes. NovaSuite integrates with Slack on the Business plan and above. You can configure notifications for new tickets, SLA breaches, agent mentions, and ticket assignments to appear in Slack channels or direct messages. The integration is set up through OAuth in the NovaSuite admin panel.

### Can customers submit tickets without creating an account

Yes. You can enable guest ticket submission that only requires an email address. You can also require customers to create a contact account before submitting. This setting is configurable under Settings, then Help Desk, then Ticket Submission Policy.

### Is there a mobile app

Yes. NovaSuite has native apps for iOS on the App Store and Android on Google Play. The mobile app supports ticket management, push notifications, quick replies, and knowledge base browsing. Workflow automation and advanced analytics are available on the desktop version only.

### Can I export my data

Yes. All plans support data export in CSV or PDF format from the Reports module. A full data export covering tickets, contacts, articles, and audit logs is available under Settings, then Data Management, then Export. Enterprise customers can configure automated exports to Amazon S3 or SFTP.

### How does the knowledge base search work

The knowledge base uses full-text search with relevance ranking across all published articles. Search indexes are updated in real time when articles are created or edited. On Business and Enterprise plans, AI-powered semantic search is available as a beta feature. Semantic search understands the intent behind a query rather than relying solely on keyword matching.

## Security and Compliance

### Is my data secure

Yes. All data is encrypted at rest using AES-256 and in transit using TLS 1.3. Customer data is logically isolated within the multi-tenant infrastructure. Physical servers are hosted on AWS in data centers that are certified for SOC 2 Type II compliance.

### Does NovaSuite support Single Sign-On

SSO is available on the Business plan and above. NovaSuite supports SAML 2.0 and OAuth 2.0 and works with identity providers including Okta, Azure Active Directory, Google Workspace, and OneLogin.

### Is NovaSuite GDPR compliant

Yes. NovaSuite is fully GDPR compliant. Features supporting GDPR include right-to-erasure request processing, full data export for any contact, configurable data retention policies, and a Data Processing Agreement available on request. EU customers can choose to have their data stored exclusively in Frankfurt, Germany.

### Is NovaSuite HIPAA compliant

HIPAA compliance is available for Enterprise customers who sign a Business Associate Agreement. This includes enhanced audit logging, restricted data access controls, and data stored in a dedicated HIPAA-eligible AWS environment.

### What happens to my data if I cancel

After cancellation, your data is retained in read-only mode for 30 days. During this period you can export all your data. After 30 days, all data is permanently and irreversibly deleted from NovaSuite servers in accordance with the data retention policy.

## Technical Questions

### Does NovaSuite have a REST API

Yes. Read-only API access is available on the Growth plan. Full read and write API access is available on Business and Enterprise plans. API documentation is available at docs.novasuite.io/api.

### Are there rate limits on the API

Yes. The Growth plan allows 100 API requests per minute. The Business plan allows 500 requests per minute. Enterprise plans can negotiate custom limits up to 5000 requests per minute. Exceeding the rate limit returns a 429 Too Many Requests response.

### Does NovaSuite support webhooks

Yes. Outbound webhooks are available on Business and Enterprise plans. You can configure webhooks to fire on events such as a ticket being created, a ticket being resolved, a CSAT rating being submitted, or an article being published. Webhooks support custom headers and HMAC signature verification for security.

### Can NovaSuite be deployed on-premise

On-premise deployment is available exclusively for Enterprise customers. It uses a Docker-based setup and requires a minimum of 8 virtual CPUs, 16 gigabytes of RAM, and 100 gigabytes of SSD storage. NovaSuite provides Docker images, deployment documentation, and setup support as part of Enterprise onboarding.

### What is the uptime SLA

The Starter, Growth, and Business plans include a 99.95 percent monthly uptime SLA. The Enterprise plan includes a 99.99 percent monthly uptime SLA. SLA credits are applied automatically if uptime drops below the guaranteed threshold. Real-time system status is available at status.novasuite.io.

## Support

### How do I get support

Support access depends on your plan. Starter plan users have access to community forums and documentation only. Growth plan users receive email support with a 24-hour response time. Business plan users receive priority email and live chat support with a four-hour response time. Enterprise users receive 24/7 phone and email support with under one hour response time for critical incidents.

### Is there onboarding help available

Yes. Business plan users get a guided onboarding email series and access to weekly live group onboarding webinars. Enterprise customers receive dedicated onboarding sessions with a Customer Success Manager, including team training and hands-on configuration assistance. Growth plan customers can purchase priority onboarding as a one-time add-on for 499 dollars.
