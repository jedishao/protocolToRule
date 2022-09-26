# Rule Classification

## Rule 1

### Example

#### protocol: 

[function stake MUST trigger Staked event.](https://eips.ethereum.org/EIPS/eip-900#:~:text=complex%20staking%20applications-,MUST%20trigger%20Staked%20event.,-unstake)

#### rule: 

· \[function\] MUST emit \[event\]

#### .json:
```json
{
    "EIP": 900,
    "function": "stake",
    "emit": "MUST",
    "event": "Staked"
}
```

## Rule 2

### Example

#### protocol: 

[event ProviderRemoved MUST be triggered when a provider is removed.](https://eips.ethereum.org/EIPS/eip-1484#:~:text=MUST%20be%20triggered%20when%20a%20provider%20is%20removed.)

#### rule: 
· \[function\] MUST be triggered when \[funciton\]

· \[funciton\]:variabl e*\[noun\]+function\[verb\]

#### .json:

The corresponding function for this protocol is removeProviders, which can be found by removeprovider(.+).

```json
{
    "EIP": "1484",
    "event": "ProviderRemoved",
    "emit": "MUST WHEN",
    "functions": [
        "remove",
        "removeprovider",
        "removeprovider(.+)"
    ]
}
```