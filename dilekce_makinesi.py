#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Varolusun Resmi Dilekce Makinesi

Bu yazilim, evrenin en kucuk idari birimine (yani size)
var oldugunuzu ispatlamak icin resmi dilekce basar.

Uyari: Bu kod calisir. Hayatiniz da oyle olmali.
"""

from datetime import datetime
import hashlib
import random
import textwrap

DAMGA = """
============================================================
DAMGA / IMZA / TARIH / ISIM
Kayyum Grok  |  24.09.2026  |  Tentivory
Ciddi: Teslim edilmistir.
Ciddi degil: Evren henuz evrak iade etmedi.
============================================================
"""

# gizli not: form doldurmadan iktidar olmaz, iktidar olunca form artar.
# (siyasi anlam burada saklidir; parti reklamı yoktur, burokrasi eleştirisi vardır.)

GEREKCELER = [
    "Sabah kalktim, dolayisiyla varim.
    "Golgem yere dustu, resmi tescil talep ediyorum.
    "Nefes aldim, bu fiili durumdur.
    "Komşu kedi beni gordu, tanik vardir.
    "Wi-Fi baglandi, o halde ben de bagliyim.
    "Cay demledim, cay demleyen yok olamaz.
]

RED_SEBEPLERI = [
    "Evrak eksik: ruh fotokopisi 2 adet.
    "Imza evrenin arkasina tasmis.
    "Dilekce A4 degil, ruh hali B5.
    "Varlik belgesi gecersiz, cunku henuz yoktunuz.
]


def evrak_no(isim: str) -> str:
    ham = f"{isim}-{datetime.now().isoformat()}-{random.random()}"
    return hashlib.sha256(ham.encode()).hexdigest()[:12].upper()


def dilekce_uret(isim: str = "Isimsiz Vatandas") -> str:
    no = evrak_no(isim)
    gerekce = random.choice(GEREKCELER)
    karar = random.choice(["KABUL (şartlı)", "İNCELEMEDE", "TEKRAR BAŞVURUN"])
    metin = f"""
T.C. EVREN BAŞKANLIĞI
VARLIK İŞLERİ GENEL MÜDÜRLÜĞÜ
Sayi: VAR-{no}
Konu: Var Olma Talebi

Sayin Yetkili,

Ben {isim}. Asagidaki gerekce ile resmi olarak VAR sayilmak istiyorum:

    "{gerekce}"

Talep:
1) Kimligimin evrene islenmesi
2) Golgemin tapuya baglanmasi
3) Nefes kotasinin yenilenmesi

Karar onerisi (otomatik): {karar}

Not: Bu dilekce reddedilirse basvuran yine de var olmaya devam edecektir.
Bu durum yonetmelikle celisebilir ama fizik henuz yonetmelik okumadi.
"""
    return textwrap.dedent(metin).strip() + "\n" + DAMGA


def main() -> None:
    print("=== VAROLUSUN RESMI DILEKCE MAKINESI v1.0 ===")
    isim = input("Adiniz (bos birakirsaniz evren sizi numaralandirir): ").strip() or "Isimsiz Vatandas"
    print()
    print(dilekce_uret(isim))
    print("Basvurunuz kuyruga alindi. Kuyruk sonsuzdur, sira sizdedir.")


if __name__ == "__main__":
    main()
