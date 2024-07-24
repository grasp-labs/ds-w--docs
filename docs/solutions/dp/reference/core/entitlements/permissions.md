# Data Platform Entitlement Service
The data platform permission system has two key components:

1. Entitlements: Group and service access management.
2. Access Control Lists: Data access management.

Data platform permissions is regulated by the `entitlements` service. Entitlements
allow administrators to define groups and regulate permissions to services.

Access Control Lists (ACLs) are used to define permissions to data. ACL can be defined
and regulated by administrators much the same way as permissions to services.

## Entitlements Service
Entitlements is a service that allows administrators to define groups and
regulate permissions. In simple terms, entitlements is a service that can be
used to give access to services to a group of users.

[Read more](./GroupMemberships.md:include)

## Access Control Lists
Access Control Lists (ACLs) are used to define permissions to data. ACL can be
defined and regulated by administrators much the same way as permissions to
services.

## FAQ

This section is to guide you through various error messages you may get when doing
various queries and operations on our Data platform.

> *I get a 403 when I try to load through the Load API.*
>
> Check if your user is part of the service.load.admin or service.load.user
> entitlement groups. You can easily do this through the Data Platform dashboard
> by going to Access Control under Management.

> *When I try to load products I have purchased, I get a 401 status with the
> message; Invalid issuer.*
>
> When you purchase a product, you are prompted to select default data owners
> and members under Access Control. Usually the owners are the admin group and
> the members are the viewer group. You can check this on Product Management by
> clicking on Access Control on a product. There you can also add groups to the
> access control if it is incorrect or missing this.
