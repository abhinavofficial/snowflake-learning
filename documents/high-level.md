# High Level Overview of Snowflake

## Cloud data warehousing platform
## SaaS
## Benefits
* No physical hardware
* Virtually no software
* Self manage
    * Maintenance
    * Management
    * Upgrades
    * Tuning

## Architecture
Three distinct area:
### Database Storage
* Schemas, a logical grouping of tables, views, functions, procedures, etc.
* Database, a logical grouping of schemas.

### Query Processing
Virtual Warehouse - CPU, Memory and temporary storage to perform operations.

Some of these operations
* Retrieving rows and columns from tables and views
* Creating tables and views
* Updating rows and columns
* Loading data
  using snowflake credits

### Cloud Services
Activities like
* Authentication
* Infrastructure management
* Access control
* Metadata management
* Query processing

## Editions
Based on
* Usage and specific requirements
* Easy to change from one edit to another
* Credit unit cost and data storage
* Account region and type - on-demand (pay per use) and capacity (upfront cost)

### Standard Edition
* SSO
* Oauth
* MFA
* Object level access control
* Time travel up to 1 day
* DR for 7 days over time travel provision

### Enterprise edition
* Stand edition +
* Time travel to 90 days
* Column level security
* Row level access from query
* Object tagging for track sensitive data and resource usage more easily

### Business Critical and VPS edition
* Enterprise edition +
* Higher security
* PHI (protected health information ) in accordance to HIPPA and HITRUST, CSF certifications and regulations
* Customer managed encryption
* VPS additionally
    * Dedicated metastore store
    * Pool of dedicated compute resources used in Virtual warehouses
    * Separate snowflake environment