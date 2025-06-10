# Attributes

## Issuer

The Issuer serves as an account-level signature, identifying who is responsible for creating an object and managing its lifecycle.

When an active tenant creates an object (via POST), it automatically assigns itself as the issuer of that object.

The issuer is stored as a plain text field, typically derived from the tenant's name.

### Sanitazion

To ensure the issuer name is clean and consistent, it may be normalized using the following function, which filters out everything except lowercase a–z characters and whitespace:

```go
func (c Context) Repr(input string) string {
	var b strings.Builder
	for _, r := range input {
		if (r >= 'a' && r <= 'z') || unicode.IsSpace(r) {
			b.WriteRune(r)
		}
	}
	return b.String()
}
```
