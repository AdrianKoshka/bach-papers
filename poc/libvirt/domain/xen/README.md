# Xen

Examples of libvirt xen domains written in bach, with their respective orginal
XML counterparts from [libvirt.org](https://libvirt.org/drvxen.html#xmlconfig).

## Structure

```
.
|-- fvgbb.{bach,xml}
|-- fvgdkb.{bach,xml}
|-- pvgb.{bach,xml}
`-- pvgdkb.{bach,xml}
```

- `fvgbb.{bach,xml}` Fullyvirtualized guest BIOS boot
- `fvgdkb.{bach,xml}` Fullyvirtualized guest direct kernel boot
- `pvgb.{bach,xml}` Paravirtualized guest bootloader
- `pvgdkb.{bach,xml}` Paravirtualized guest direct kernel boot
