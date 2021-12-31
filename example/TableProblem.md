---
title: "Hunting down Problems with table skipping"
author: "Norman Markgraf"
date: "26.12.2018"
output: pdf_document
---

## A short Example of an error

The next slides includes a table and should be skipped

## This slide will not be displayed {exclude=all}

|   | Testentscheidung $H_0$ nicht verwerfen| Testentscheidung $H_0$ verwerfen  |
|:---|:---:|:---:|
| Realität: $H_0$  | Ok | **Fehler 1. Art**^[Auch $\alpha$-Fehler genannt.  Die Wahrscheinlichkeit dieses Fehlers wird durch das Signifikanzniveau nach oben beschränkt.] |
| Realität: $H_A$  | **Fehler 2. Art**^[Auch $\beta$-Fehler genannt.  Die Wahrscheinlichkeit dieses Fehlers ist schwieriger zu bestimmen, aber siehe z. B. Paket [pwr](https://cran.r-project.org/package=pwr). Bei guten Tests sinkt sie mit größerem Stichprobenumfang $n$.]  | Ok  |

## This is the slide after the table slide

And this should be displayed!

## And this slide will not be displayed also! {exclude=all}

|   | Testentscheidung $H_0$ nicht verwerfen| Testentscheidung $H_0$ verwerfen  |
|:---|:---:|:---:|
| Realität: $H_0$  | Ok | **Fehler 1. Art**^[Auch $\alpha$-Fehler genannt.  Die Wahrscheinlichkeit dieses Fehlers wird durch das Signifikanzniveau nach oben beschränkt.] |
| Realität: $H_A$  | **Fehler 2. Art**^[Auch $\beta$-Fehler genannt.  Die Wahrscheinlichkeit dieses Fehlers ist schwieriger zu bestimmen, aber siehe z. B. Paket [pwr](https://cran.r-project.org/package=pwr). Bei guten Tests sinkt sie mit größerem Stichprobenumfang $n$.]  | Ok  |
