
Stripe: how to runout a Subscription
--

It's easy to create or delete/cancel a subscription immediately. But what about the case of cancelling a subscription but letting the service run until the end of the billing cycle?

Turns out this is not too difficult: Stripe has the concept of a 'SubscriptionSchedule' object. we'll use this to cancel the subscription immediately but keep it running - as required.

https://docs.stripe.com/billing/subscriptions/subscription-schedules

```python
subscriptions = stripe.Subscription.list(customer=CUSTOMER_ID)
for subscription in subscriptions.data:
    if 'Cancellable' in subscription.metadata.keys():
        subscription_schedule = stripe.SubscriptionSchedule.create(
            from_subscription=subscription.id,
        )
        stripe.SubscriptionSchedule.modify(
        subscription_schedule.id,
            end_behavior="cancel")
```

Notes:
* This uses the 'metadata' field: the customer may have multiple subscriptions & we may want to cancel all of them. Or not!
* The docs suggest this 2-step 'create' then 'modify' approach. Doing the creation in one step indeed didn't work for me.
* If the customer were to re-subscribe during this run-out period, then the proper thing to do would be to cancel the subscription-schedule instead of creating a new subscription.