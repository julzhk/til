TIL : new colour spaces
---

I've done enough CMYK printing (and been surprised often enough with how different it looks from what I see on my screen (if you know you know!)) to be interested in colour on the web..

Seems there's a new game (gamut?) in town, with the introduction of [OKLCH](https://jakub.kr/components/oklch-colors)

Why use it?
* slightly wider gamut than RGB (eg can show more colours.)
* apparently more perceptually uniform & more accurate to human perception

What this means is when a series of colours are presented they can be automatically/mathematically-obviously consistent. If you want to lighten a red and blue - and want the two new colours to be 
still consistent - OKLCH makes this convenient.

Can it be used in modern browsers and TailwindCSS? [Yep!](https://1902.studio/journal/using-oklch-colors-in-tailwind-css). And this is a [fun tool](https://lch.oklch.com/#0.836,58.32,169.03,0). 
What does it do? Not sure, but it's cool.

