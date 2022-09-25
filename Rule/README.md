# Rule Classification

## Rule 1

### Example

#### protocol: [function stake MUST trigger Staked event.](https://eips.ethereum.org/EIPS/eip-900#:~:text=complex%20staking%20applications-,MUST%20trigger%20Staked%20event.,-unstake)

#### rule: \[function\] MUST emit \[event\]

#### .json:
```json
{
    "EIP": 900,
    "function": "stake",
    "emit": "MUST",
    "event": "Staked"
}
```