> # 0x19-postmortem
---

<p align="center"><a href="url"><img src="https://images-na.ssl-images-amazon.com/images/I/71q9Q6EYa4L._AC_SL1500_.jpg" width="360" height="480"></a></p>

---

## Rappi Orders-API purchase mismatch report

## Issue summary:

From 7:32 PM to 8:12 PM (GMT), purchase requests resulted in an order mismatch, in which all clients, instead of their desired order, received a “World’s Worst Person” mug, from “Craig’s Gifts n’ Gags” store. The issue affected 100% of orders while the misconfigured API was functioning.  

## Timeline (All times Greenwich Mean Time):

* Timeline (All times Greenwich Mean Time)
  * 7:32 PM: API configuration pushed and orders request start.
  * 7:39 PM: Purchase Checker alerts Marketing Team of orders surge in specific item. 
  * 7:48 PM: Customer Satisfaction System alerts massive increment of customer complaints.
  * 8:03 PM: Configuration rollback failed.
  * 8:12 PM: User specific servers disabled.
  * 8:14 PM: Configuration rollback successful, servers back up.

## Root Cause

At 7:32 PM (GMT), a configuration change in our Orders API was pushed to our production environment without being first released to our test environment. The change invalidated how our Orders-API handled JSON conversions from customer input, and reverted said process to a scenario explicit for testing in which the aforementioned item’s (mug) purchase information was used as default JSON output. In addition, since all orders where being placed for that specific product, the database which stores the information processed by our Purchase Checker, collapsed. Our customer Satisfaction System was also overloaded. These failures impeded the first configuration rollback attempt at 8:03 PM from being successful, for which we had to disable user specific servers at 8:12 PM. Some users received a `503-server overload` error.

## Resolution and recovery

At 7:39 and 7:48 the Purchase Checker and Customer Satisfaction System, respectively, alerted us of our mistake. Since both were being overloaded by the massive ordering of the same product (a product known to the API’s Program Strategy department because of their heavy use of it in tests), we were able to detect the error instantly. A configuration was ready to be released at 8:10 PM, but since both the Purchase Checker and Customer Satisfaction System databases had collapsed, we had to disable them at 8:12 PM. Both servers were set a cap for storing information regarding specific products, and the Orders API was rolled back to its previous, working iteration. This allowed us to get the API and disabled servers back up and working properly at 8:14 PM.

## Corrective and preventive measures

In the last three days, we’ve conducted an internal review and analysis of the outage. The following are actions we are taking to address the underlying causes of the issue and to help prevent any recurrence of any foreseeable issues:

* Disable the current configuration release mechanism and replace it for a safer, preferably human overseen, one.
* Make rollback processes independent of server functionality.
* Review and add caps to all overloadable databases (Finished).
* Improve departments communications inside Rappi.
* Develop mechanism to better communicate to our customers the status of our app, as well as what we are doing to fix it.

Rappi is committed to always deliver a quick and reliable experience to our users. We appreciate and apologise to everyone who received said product (the “World’s Worst Person” mug), and will refund all of those purchases. Our users are also incentivised to keep the mug and invest on “Craig’s Gifts n’ Gags” shop, which is now set to be listed on the Nasdaq. 

---
> ## Contact 

| [Twitter](https://twitter.com/David__Persona) | [LinkedIn](www.linkedin.com/in/christian-david-campos/) | [Mail](1566@holbertonschool.com) | [Github](https://github.com/ChristianCampos-55) |
|---|---|---|---|

---

## License
*`postmortem` is open source and therefore free to download and use without permission.*

---
