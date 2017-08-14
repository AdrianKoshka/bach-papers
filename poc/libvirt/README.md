# Libvirt PoCs

This is mostly filled with converted example code from [libvirt.org](https://libvirt.org).
So while I suppose these are "Proof of Concepts", don't expect anything amazing.

## Structure

```
.
|-- domain
|   |-- kvm
|   `-- xen
|-- network
`-- storage
```

- `domain` defining libvirt domains
  - `kvm` KVM/QEMU domains
  - `xen` Xen domains
- `network` defining libvirt networks
- `storage` defining storage pools and volumes
