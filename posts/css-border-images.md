TIL : images for a border in CSS
-

I don't use CSS extremely regularly, so I'm frequently surprised by what's possible with it.  Today's minor surprise: 

```css
border-image-repeat: round;
```

[This tiles an image on a border.](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-repeat)

And fortunately [it's available in tailwinds css too](https://tailwindcss.com/docs/background-repeat#preventing-clipping)

---
<section>
  <div style="width:240px;height:120px;border:16px solid transparent;border-image:url('https://via.placeholder.com/40') 16 round;">
    Inline CSS example: border-image-repeat: round;
  </div>
</section>