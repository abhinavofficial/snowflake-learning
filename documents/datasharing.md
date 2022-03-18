# Data Sharing

## Shares Inbound
* You have the shared by column, which tells you the name of the share provider's account.
* You have the secure share name, which is the name given to each share by the provider.
* And last, you have the database, which is the name you see when you're looking at your list of databases.

> Account Usage Share, also called Snowflake database is special and is the way Snowflake interacts with users
> Inbound Share privileges are imported. You cannot run SQL DDL on inbound shares. Shared data is Read-ONLY

Tabular format on what you can and cannot do:

|                              | Most Inbound Shares | Account Usage Share | Regular Database |
|------------------------------|---------------------|---------------------|------------------|
| **Based on a Share**         | Y                   | Y                   | N                |
| **Drop Database**            | Y                   | Y                   | Y                |
| **Create Database**          | Y                   | N                   | Y                |
| **Rename Database**          | Y                   | N                   | Y                |
| **Add Comment**              | Y                   | N                   | Y                |
| **Grant Specific privilege** | N                   | N                   | Y                |
| **Grant ALL**                | N                   | N                   | Y                |
| **Revoke ALL**               | N                   | N                   | Y                |
| **Grant IMPORTED**           | Y                   | Y                   | N                |
| **Revoke IMPORTED**          | Y                   | Y                   | N                |
| **Create Schema**            | N                   | N                   | Y                |
| **Alter Table**              | N                   | N                   | Y                |
| **Drop Stage**               | N                   | N                   | Y                |
| **Create Sequence**          | N                   | N                   | Y                |
| **Alter View**               | N                   | N                   | Y                |
| **Use in select**            | Y                   | Y                   | Y                |
| **Use in Join**              | Y                   | Y                   | Y                |
| **Filter (Where)**           | Y                   | Y                   | Y                |
| **Aggregate (Group)**        | Y                   | Y                   | Y                |
| **Download/Export**          | Y                   | Y                   | Y                |
| **Insert/Update/Merge**      | N                   | N                   | Y                |

## Outbound shares
The data can be shared by Snowflake customers to their customers using a reader or managed account when their customer are not Snowflake customer. _Not sure what the cost to reader org is though_

### Managed Account? Reader Account? Sub-Account?
All three terms refer to the same, limited, account type. The account can be called a sub-account because it is owned by your Trial Account (a full account) instead of being directly owned and managed by Snowflake. As a sub-account, owned by your Trial Account, you must manage it. As manager of the account you can restrict USERS to "read-only" permissions like selecting and downloading.

## Security Tips
* Don't keep passwords in a plain text file
* Don't write your passwords on a paper you keep on your desk
* Don't reuse the same password
* Follow the password policies outlined by your work organization

## Shopping the Data Marketplace

Two types of purchase: **Standard** and **Personalized**. Similarly, Marketplace, there are two types of tiles: **Free** or **Standard** and **Personalized Data**.

A listing is a share of data which is displayed on a tile which are packaged like product. Provider are companies which product data who monetize the data.

"Personalized" refers to the sharing process. "Customized" refers to the data you receive.

Personalized listings have a process flow that includes some payment negotiations, service level agreements, and other legal considerations. Your path to receiving the data set will be very individualized. The share you end up with might be exactly the same as thousands of other customers but the paperwork you signed is likely to be individually distinct. The truth about Personalized flows is that they are mainly to allow providers to collect money for data (until Snowflake completes development of an in-app payment functionality).  So, just keep this in mind and don't try to come up with an idea for customized data.

Data received via a Personalized listing MIGHT be customized to a certain region, or for a set of characteristics you choose as a consumer, but that is not always the case.  Do not confuse the two and do not try to offer a Customized data set with your Personalized listing.

## Marketplace requirement
* Fresh
* Real
* Legally Shareable

Next step data sharing agreement

> Expanding your simple, free data set into something worth paying for! Example: Adding more rows and columns of value or a complimentary table
> Name your dataset for **exactly what it does**. Being too creative can be a pitfall. Add a limiter - something that describes why your free data set is so small. Use Init Cap (capital letter for almost every word in title). Your paid-for data set should have a name that sounds like it's worth paying for.
> Free Data Should NEVER include Personal Information!
> Free Data Should NOT include Volatile Information!
> Avoid Weak Words! Avoid Filler Words!
> Do NOT use a naming pattern alike Basic and Premium. 
> Do not use Basic and Enhanced. 
> Do not use Basic and Extended. 
> In fact, do not use the word Basic at all, ever. 
> Do not use Premium, Enhanced, Extended, Advanced, Detailed or Details.

All of these are just a way to avoid being more specific. Spend a few minutes thinking about what information will attract "shoppers" and use those words instead of weak words like "basic" and "premium"!

Other weak words include filler words. You also really don't need words like "List of" or "Data" in a listing title. Every listing is made of data.

> Phrases like "List of" aren't necessary. You could use the same space to tell us more interesting things about your data set.
> "Information" and "Data" are not very informative in listing titles (they are okay in Provider Names). Every listing on an exchange has data, every listing has information.

Free data, think small. Pair-for set, think big.


## Data Exchange
* Invitation Only
* Customer Controlled
* Efficient Maintenance
When sharing restricted data between organization data

Three roles:
* Admin Role
* Provider Role
* Consumer Role

Requesting an Exchange requires
* Admin Account URL
* Exchange Name