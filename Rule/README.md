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
· \[event\] MUST be triggered when \[funciton\]

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

## Rule 3

### Example

#### protocol: 

[While a Sent event MUST NOT be emitted when minting.](https://eips.ethereum.org/EIPS/eip-777#:~:text=While%20a%20Sent%20event%20MUST%20NOT%20be%20emitted%20when%20minting.)

#### rule: 
· \[event\] MUST NOT be emiitted when \[funciton\]

· \[funciton\]:variable

#### .json:

```json
{
    "EIP": "777",
    "event": "Sent",
    "emit": "MUST NOT",
    "functions": [
      "mint"
    ]
}
```