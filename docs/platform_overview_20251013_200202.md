# Platform Overview

Our platform is a cohesive, event-driven system for moving, transforming, storing, and serving data securely and efficiently. Each service is designed to be simple to use on its own and even more powerful when combined with the others.

## Clone
Clone moves your data wherever you need it—automatically. Whether it’s syncing between AWS, Azure, or Google Cloud, Clone keeps your data fresh and consistent across systems. It reacts to events, runs on a schedule, or follows your workflows, making data movement effortless and always up to date. You choose the source and destination—Clone takes care of the rest.

## Workflow
Workflow makes building ETL pipelines fast and intuitive. Using a no-code interface or ready-made templates, you can define datasets, connect data sources, and transform data with familiar operations like join, merge, and filter. It’s powered by in-memory processing for efficiency, integrates with State Service and other computing blocks, and lets anyone build reliable, stateful data flows in minutes.

## Pipeline
Pipeline delivers ready-to-use data straight to your tools. Choose from over 15,000 validated datasets, set when and where they run, and send them to Azure Blob, Power BI, or your own database. Every dataset is pre-validated, deduplicated, and performance-optimized. With flexible configuration and low cost, Pipeline makes data delivery both powerful and effortless—ready the moment you need it.

## State Service
State Service keeps your workflows and applications aware of where they are. It’s a fast, in-memory key-value service that stores and retrieves state instantly, enabling smooth, stateful experiences across the platform. Built for low latency and reliability, it connects directly to Workflow, Pipeline, and Clone, ensuring everything runs consistently and efficiently from one state to the next.

## Message Service
Message Service connects everything in an event-driven platform powered by Kafka. Sending a message is how you trigger an action—start a workflow, move data, or run a job on demand. Events flow in real time between all components, keeping the system responsive and coordinated. Simple, scalable, and fast, Message Service is the backbone that keeps the entire platform in sync.

## Fetch Service
Fetch Service is the simplest way to access your data. Built on a fast, reliable Go Echo REST API, it lets you query and retrieve any dataset stored on the platform. All data from your configured pipelines and integrations automatically lands in our secure data lake, where it’s validated, organized, and ready for use. With Fetch Service, you can access this data directly—on demand—whether you’re building dashboards, running analysis, or integrating with external systems.

## Store Service
Store Service is the catalog of everything on the platform—the single place where all products, schemas, and metadata live. If the platform were a supermarket, Store would be the shelves holding every product, complete with details, structure, and pricing. Built around our love for schemas, Store ensures consistency and clarity across all components, so every dataset, pipeline, or service knows exactly what it’s working with.

## Config Service
Config Service is where you define what the platform delivers for you. It holds all your user configurations—the connections, schedules, parameters, and setup details that determine how your data flows and systems operate. Every block in the platform relies on Config to know what to do and how to do it. Config integrates with Vault Service, ensuring all sensitive credentials and keys referenced in your configurations are stored and accessed securely.

## Vault Service
Vault Service is the secure foundation for managing all secrets, keys, and credentials on the platform. It uses modern cryptographic standards—including envelope encryption, key-encryption keys (KEK), data-encryption keys (DEK), and one-way hashing—to ensure your secrets are never exposed in plain form. Vault integrates directly with Config Service, so configurations can safely reference the secrets they need without compromising security.

## Identity Service
Identity Service manages who you are on the platform. It handles user authentication, profiles, and access context, ensuring every interaction is secure and personalized. When you sign in, create a connection, or execute a job, Identity verifies and represents you consistently across all services.

## Entitlement Service
Entitlement Service controls what each identity can do. It’s the platform’s permission and policy layer—managing access through groups, roles, and grants, similar in spirit to systems like Microsoft Entra. With Entitlement, you can define fine-grained permissions for users, services, and operations, keeping collaboration secure and organized.

## Health Service
Health Service keeps your systems reliable by continuously checking that everything is working as expected. Configure custom health checks for IPv4 or IPv6 addresses, URLs, database hosts, or API endpoints, and validate expected results—not just availability. Health Service integrates with the rest of the platform to provide real-time visibility into the status of your data sources, pipelines, and applications.
