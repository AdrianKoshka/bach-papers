# Network

Various example network configurations implimented in bach.

## Structure

```
.
|-- eb.{bach,xml}
|-- isolated.{bach,xml}
|-- isolated6.{bach,xml}
|-- macvtap.{bach,xml}
|-- nat.{bach,xml}
|-- nat-dhcpv6.{bach,xml}
|-- nga.{bach,xml}
|-- rn.{bach,xml}
|-- rn-dhcpv6p.{bach,xml}
`-- rn-hdv6.{bach,xml}
```

- `eb` Using an existing host bridge
- `isolated` A completely isolated network for guests
- `isolated6` A completely isolated ipv6 network for guests
- `macvtap` A macvtap "direct" connection
- `nat` NAT based network
- `nat-dhcpv6` NAt based network with ipv6 dhcpv6 definition
- `nga` Network config with no gateway address
- `rn` a routed network with ipv4/6
- `rn-dhcpv6p` a routed network with ipv6 only
- `rn-hdv6` a routed network with ipv6 host definitions
