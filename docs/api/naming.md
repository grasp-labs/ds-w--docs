# Naming conventions and guidelines

These guidelines and conventions are exactly that: guidelines, not rules.

## Guidelines

1. Prefer simple, concise, and intuitive names.
2. Prefer lower-case, hyphen-separated names.
3. Prefer single-word names.
4. Prefer 7-bit ascii.
5. Prefer singleton form.

### Simple, concise and intuitive

Simple and concise names are easy to remember, easy to talk about, and aid communication. If possible, avoid non-standard abbreviations and avoid overloading names - prefer different names for different concepts.

Some name reuse is unavoidable, in which case there should be sufficient context available for the concept itself to become unambiguous.

### Lower-case, hyphen-separated

URLs are case sensitive, except for the host component, but in practice a lot of systems are still case insensitive (like IIS).

To help reduce friction, prefer lower-case hyphen-separated names, both in URLs and possibly fields. 

The hyphen (-) is preferred over the underscore (_), since the underscore in some fonts and renderers is difficult to separate from the whitespace and leaves no room for doubt. Hyphen is not [escaped](https://www.ietf.org/rfc/rfc1738.txt) in an URL so is well suited as a word separator.

### 7-bit ascii

Using 7-bit ascii is the recommended and safest choice. URLs are defined by [RFC 3986](https://datatracker.ietf.org/doc/html/rfc3986), which restricts allowed characters to a subset of 7-bit ASCII. And it is universally supported across browser, web servers, networking libraries and operating systems.

### Singular singleton form

A resource is the fundamental concept of a REST API. A resource is an object with data, types, relations to other objects, etc. Resources can be grouped into collections or exist on their own.

Resource can be accessed and manipulated by a combination of http methods and resource identifier ([URI](https://en.wikipedia.org/wiki/Uniform_Resource_Identifier)).

As suggested we prefer singular form of resource naming (i.e. `product` rather than `products`).

__to_be_discussed__: In some cases, the plural form makes it easier to achieve consistent naming across endpoint operations on different cardinalities.

Plurality indicates the resources are regarded as collections, which conceptually makes sense (singleton resources can be treated as a collection with cardinality 1, but not the other way).

```
GET https://daas-servcie.com/api/store/products/ should return a collection products.
GET https://daas-servcie.com/api/store/products/{product-id}/ should return a single products with the given product id.
POST https://daas-servcie.com/api/store/products/ should submit a product entity to the products resources.
```