# User Guide on our Log service API

## General information

### About logs
Just about every flow, pipeline and service on the Data Platform has an AWS Log
group. In these, there are log streams that represents the sequence of events
coming from an application instance or a resource on DP. Through these logs we
can  monitor errors, trace back the occurrence of the failure and from there
easily debug.

### On Data Platform
From Monitoring -> Logs Explorer you can freely search through Data Platforms'
various log groups. Here you can choose log group to explore, the time frame you
want to explore, and type in search fields you are looking for. For example, if
you did a full load on a Brreg dataset and want to check  the process; you would
look at */aws/lambda/daas-service-injection-brreg-dev* and
*/aws/lambda/daas-service-transform-brreg-dev* log groups within 10-15 min of
when you ran the full load. In return, you would get a list of all log streams
in this group within the chosen period.

You can also access the Logs Explorer through the Dashboard Analysis by
inspecting a failed pipeline and click 'See logs'. This way, you are redirected
to the explorer with the relevant log group, time period and search filer.

### On Postman
If you prefer a more traditional way, you can use postman or any other API
platform to query the Log service API.
