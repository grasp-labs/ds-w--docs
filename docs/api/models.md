# Models

## Health Check

```go
type HealthCheck struct {
	Message string `json:"message" example:"Server is running."`
	Time    string `json:"time" example:"2006-01-02T15:04:05Z07:00"`
}
```

## ORM

```go
type BaseModel struct {
	ID          uuid.UUID  `gorm:"type:uuid;primaryKey" json:"id"`
	Issuer      string     `json:"issuer"`
	Name        string     `json:"name"`
	Version     string     `json:"version"`
	Description string     `json:"description"`
	Status      ItemStatus `json:"status"`
	Metadata    string     `json:"metadata"`
	Tags        string     `json:"tags"`
	CreatedAt   time.Time  `json:"created_at"`
	ModifiedAt  time.Time  `json:"modified_at"`
	CreatedBy   string     `json:"created_by"`
	ModifiedBy  string     `json:"modified_by"`
}

func (t *BaseModel) Validate() []ValidationError {
	var errors []ValidationError
	switch t.Status {
	case Active, Deleted, Suspended, Rejected, Draft:
	// Ok
	default:
		errors = append(errors, ValidationError{
			Field:   "Status",
			Message: "Invalid.",
		})
	}
	return errors
}

// Example implementation of Base model 
type Target struct {
	BaseModel
	Data TargetData `json:"data"`
}
```
