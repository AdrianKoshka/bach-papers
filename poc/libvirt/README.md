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

- `domain` defining libvirt [domains](https://libvirt.org/formatdomain.html)
  - `kvm` KVM/QEMU domains
  - `xen` Xen domains
- `network` defining libvirt [networks](https://libvirt.org/formatnetwork.html)
- `storage` defining [storage pools and volumes](https://libvirt.org/formatstorage.html)

## Other libvirt Schemas

There are a few of schemas belonging to libvirt that I probably am not going to
cover only because at this point, it should be obvious to anyone who's
understood how to impliment any of the shcemas I've covered thus far. Though I
will list the ones I haven't covered.

- [Network filtering](https://libvirt.org/formatnwfilter.html)
- [Storage encryption](https://libvirt.org/formatstorageencryption.html)
- [Capabilities](https://libvirt.org/formatcaps.html)
- [Domain Capabilities](https://libvirt.org/formatdomaincaps.html)
- [Node devices](https://libvirt.org/formatnode.html)
- [Secrets](https://libvirt.org/formatsecret.html)
- [Snapshots](https://libvirt.org/formatsnapshot.html)

## Validator / Parser

> libvirt provides a tool called `virt-xml-validate`, which uses the locally installed RNG (Relax-NG) schema documents, and also auto-detects which schema to validate based on the top level element. (Roughly paraphrased from libvirt.org/format.hmtl)

Something like this but for libvirt documents written in bach would be
execellent, though not really my thing. I suppose another thing that would be
needed would be something to convert libvirt documents written in bach to
their original XML counterparts.
