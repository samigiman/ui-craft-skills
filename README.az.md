# UI Craft Skills

**Məqsədli və özünəməxsus interfeyslər üçün 6 skill.** Sayt və tətbiq dizaynı, şablon AI görünüşünün təmizlənməsi və nəticənin real yoxlanması üçün hazırlanıb.

[English](README.md) · [Prompt nümunələri](docs/examples.md) · [MIT lisenziyası](LICENSE)

Məqsəd bütün saytları eyni ağ səhifəyə çevirmək deyil. Brend, real məzmun və istifadəçinin görməli olduğu iş əsas götürülür. Rəng, gradient, kart və animasiya öz-özlüyündə “AI slop” sayılmır.

| Skill | Nə edir |
| --- | --- |
| [`product-ui-direction`](skills/product-ui-direction/SKILL.md) | Məhsula uyğun orijinal sayt və tətbiq istiqaməti qurur. |
| [`ui-deslop`](skills/ui-deslop/SKILL.md) | Şablon görünüşü və mənasız qarışıqlığı məqsədli şəkildə təmizləyir. |
| [`reference-led-web-design`](skills/reference-led-web-design/SKILL.md) | Verilən nümunəni araşdırır, vizual uyğunluğu və tam sayt quruluşunu qoruyur. |
| [`commerce-ux-refinement`](skills/commerce-ux-refinement/SKILL.md) | Məhsul, variant, alış, qeydiyyat və hesab axınlarını aydınlaşdırır. |
| [`responsive-ui-verification`](skills/responsive-ui-verification/SKILL.md) | Mobil/masaüstü görünüşləri, vəziyyətləri və dizayn dəyişikliklərini yoxlayır. |
| [`operational-dashboard-ux`](skills/operational-dashboard-ux/SKILL.md) | Filtrləri, iş siyahılarını və real statusları anlaşılan edir. |

## Quraşdırma

Python 3.10+ və Git lazımdır. Quraşdırıcı və köməkçi skriptlər əlavə Python paketi, API açarı və MCP serveri tələb etmir; istifadə etdiyiniz agentin öz tələbləri ayrıca qalır.

```bash
git clone https://github.com/samigiman/ui-craft-skills.git
cd ui-craft-skills
python3 scripts/install.py --all --dry-run
python3 scripts/install.py --all
```

Yalnız birini quraşdırmaq üçün:

```bash
python3 scripts/install.py --skill ui-deslop
```

Mövcud skill qovluqları əvəz edilmir. Standart ünvan `$CODEX_HOME/skills`, bu dəyişən yoxdursa `~/.codex/skills` olur. Quraşdırmadan sonra yeni Codex mesajında bacarıqlar aşkarlana bilər.

## İstifadə nümunələri

```text
$ui-deslop bu saytın şablon AI görünüşünü təmizlə.
Brend rəngini, real məzmunu və işləyən funksiyaları qoru.
```

```text
$commerce-ux-refinement məhsulun rəng/RAM seçimini,
qeydiyyat və hesab ekranlarını aydınlaşdır.
```

```text
$responsive-ui-verification bu dəyişiklikdən sonra mobil və masaüstü
görünüşləri yoxla. Əvvəlki dizaynın kompozisiyasını qoru.
```

Skill təlimatları əsasən ingiliscədir; istifadəçi Azərbaycan dilində tapşırıq verə bilər. Codex `SKILL.md` formatına uyğun hazırlanıb; başqa agentlərə avtomatik inteqrasiya iddiası yoxdur.

`ui-deslop` daxilindəki skaner yalnız yoxlanmalı kod yerlərini göstərir. Faylları dəyişmir, AI mənşəyi və dizayn keyfiyyəti barədə avtomatik hökm vermir. Real dizayn nəticəsi render və istifadəçi axını ilə yoxlanmalıdır.

[İştirak qaydaları](CONTRIBUTING.md) · [Yoxlamaların əhatəsi](docs/validation.md)

Müəllif: [Samig Imanov](https://github.com/samigiman). [MIT lisenziyası](LICENSE) ilə açıq paylaşılır.
