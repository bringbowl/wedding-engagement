# -*- coding: utf-8 -*-
# Build the ornamental card frame (everything except the role/name text) as an SVG,
# then render to a high-res transparent-free PNG reused on every card.
W, H = 915, 600

SVG = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs>
  <linearGradient id="gold" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#f4e2a8"/><stop offset="0.45" stop-color="#cBA557"/>
    <stop offset="1" stop-color="#9c7a2e"/>
  </linearGradient>
  <linearGradient id="goldbr" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#f6e6b0"/><stop offset="0.5" stop-color="#cfa74f"/>
    <stop offset="1" stop-color="#9c7a2e"/>
  </linearGradient>
  <filter id="paper"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" result="n"/>
    <feColorMatrix in="n" type="saturate" values="0"/>
    <feComponentTransfer><feFuncA type="linear" slope="0.05"/></feComponentTransfer>
    <feComposite operator="over" in2="SourceGraphic"/></filter>
  <radialGradient id="ivory" cx="50%" cy="42%" r="75%">
    <stop offset="0" stop-color="#FDFaf0"/><stop offset="1" stop-color="#F4EAD2"/>
  </radialGradient>
</defs>

<!-- wine border / back -->
<rect x="0" y="0" width="{W}" height="{H}" fill="#6E1414"/>
<rect x="0" y="0" width="{W}" height="{H}" fill="#5a0f0f" opacity="0.0"/>

<!-- ivory panel -->
<rect x="26" y="26" width="{W-52}" height="{H-52}" rx="10" fill="url(#ivory)"/>
<rect x="26" y="26" width="{W-52}" height="{H-52}" rx="10" fill="#000" opacity="0.0"/>
<rect x="34" y="34" width="{W-68}" height="{H-68}" rx="7" fill="none" stroke="#C9A24B" stroke-width="1.4" opacity="0.8"/>
<rect x="40" y="40" width="{W-80}" height="{H-80}" rx="5" fill="none" stroke="#C9A24B" stroke-width="0.7" opacity="0.45"/>

<!-- GOLD FOIL CORNER BRACKETS (outer corners) -->
<g fill="url(#goldbr)" stroke="#8a6a24" stroke-width="0.8">
  <path d="M0,0 L96,0 C58,8 20,36 10,96 L0,96 Z"/>
  <path d="M{W},0 L{W-96},0 C{W-58},8 {W-20},36 {W-10},96 L{W},96 Z"/>
  <path d="M0,{H} L96,{H} C58,{H-8} 20,{H-36} 10,{H-96} L0,{H-96} Z"/>
  <path d="M{W},{H} L{W-96},{H} C{W-58},{H-8} {W-20},{H-36} {W-10},{H-96} L{W},{H-96} Z"/>
</g>
<g fill="none" stroke="#7a5c1f" stroke-width="0.9" opacity="0.6">
  <path d="M86,6 C54,14 20,44 12,86"/>
  <path d="M{W-86},6 C{W-54},14 {W-20},44 {W-12},86"/>
  <path d="M86,{H-6} C54,{H-14} 20,{H-44} 12,{H-86}"/>
  <path d="M{W-86},{H-6} C{W-54},{H-14} {W-20},{H-44} {W-12},{H-86}"/>
</g>

<!-- CROWN top center -->
<g transform="translate({W/2-95},36)">
  <g fill="url(#gold)" stroke="#8a6a24" stroke-width="1">
    <path d="M10,86 L26,44 L46,64 L95,20 L144,64 L164,44 L180,86 Z"/>
    <rect x="4" y="86" width="182" height="22" rx="5"/>
    <circle cx="26" cy="44" r="5.5"/><circle cx="95" cy="20" r="6"/><circle cx="164" cy="44" r="5.5"/>
    <rect x="90" y="2" width="10" height="20" rx="2"/><rect x="83" y="6" width="24" height="7" rx="2"/>
  </g>
  <g fill="#8a2f2a" opacity="0.85"><circle cx="52" cy="97" r="4"/><circle cx="95" cy="97" r="4.5"/><circle cx="138" cy="97" r="4"/></g>
  <line x1="8" y1="97" x2="182" y2="97" stroke="#8a6a24" stroke-width="0.8" opacity="0.5"/>
</g>

<!-- top-corner filigree scrolls (fuller) -->
<g fill="none" stroke="url(#gold)" stroke-width="2.4" stroke-linecap="round">
  <g transform="translate(60,70)">
    <path d="M0,52 C0,18 28,2 60,10 C36,12 22,32 32,50 C42,32 64,32 78,46"/>
    <path d="M32,50 C32,60 40,68 52,68"/>
    <path d="M0,52 C-4,40 4,28 18,26"/>
    <circle cx="2" cy="53" r="2.6" fill="url(#gold)" stroke="none"/>
    <circle cx="18" cy="26" r="2" fill="url(#gold)" stroke="none"/>
  </g>
  <g transform="translate({W-60},70) scale(-1,1)">
    <path d="M0,52 C0,18 28,2 60,10 C36,12 22,32 32,50 C42,32 64,32 78,46"/>
    <path d="M32,50 C32,60 40,68 52,68"/>
    <path d="M0,52 C-4,40 4,28 18,26"/>
    <circle cx="2" cy="53" r="2.6" fill="url(#gold)" stroke="none"/>
    <circle cx="18" cy="26" r="2" fill="url(#gold)" stroke="none"/>
  </g>
</g>

<!-- bottom-center flourish with two birds -->
<g transform="translate({W/2},{H-66})">
  <g fill="none" stroke="url(#gold)" stroke-width="2.4" stroke-linecap="round">
    <path d="M0,8 C-22,8 -34,-4 -62,-2 C-42,4 -38,16 -52,24 C-34,18 -20,17 0,10"/>
    <path d="M0,8 C22,8 34,-4 62,-2 C42,4 38,16 52,24 C34,18 20,17 0,10"/>
    <line x1="-26" y1="9" x2="26" y2="9"/>
  </g>
  <path d="M0,-4 L7,9 L0,4 L-7,9 Z" fill="url(#gold)"/>
  <!-- two small swallows, near centre, flying up-out -->
  <g stroke="#9c7a2e" stroke-width="2.2" fill="none" stroke-linecap="round">
    <path d="M-30,-16 q7,-8 14,-2 q7,-8 15,0"/>
    <path d="M30,-16 q-7,-8 -14,-2 q-7,-8 -15,0"/>
  </g>
</g>

<!-- POSTMARK: AIR MAIL (bottom-left) -->
<g transform="translate(118,{H-112})" opacity="0.9">
  <g fill="none" stroke="#9a4234" stroke-width="2.2">
    <circle cx="0" cy="0" r="52"/><circle cx="0" cy="0" r="43" stroke-width="1.2"/>
  </g>
  <path id="amT" d="M0,0 m-37,0 a37,37 0 0,1 74,0" fill="none"/>
  <path id="amB" d="M0,0 m-33,0 a33,33 0 0,0 66,0" fill="none"/>
  <text font-family="Georgia,serif" font-size="12.5" letter-spacing="2.5" fill="#9a4234" font-weight="700">
    <textPath href="#amT" startOffset="50%" text-anchor="middle">AIR MAIL</textPath></text>
  <text font-family="Georgia,serif" font-size="10" letter-spacing="2" fill="#9a4234">
    <textPath href="#amB" startOffset="50%" text-anchor="middle">WITH LOVE</textPath></text>
  <path d="M0,-4 C-7,-14 -22,-6 0,12 C22,-6 7,-14 0,-4 Z" fill="#9a4234"/>
  <!-- cancellation wavy lines -->
  <g stroke="#9a4234" stroke-width="2.4" fill="none" opacity="0.85" stroke-linecap="round">
    <path d="M48,-18 q18,-7 36,0 q18,7 36,0 q18,-7 30,-3"/>
    <path d="M46,-6 q18,-7 36,0 q18,7 36,0 q18,-7 32,-3"/>
    <path d="M48,6 q18,-7 36,0 q18,7 36,0 q18,-7 30,-3"/>
  </g>
</g>

<!-- POSTMARK: TAINAN (bottom-right) -->
<g transform="translate({W-118},{H-112})" opacity="0.9">
  <g fill="none" stroke="#9a4234" stroke-width="2.2" stroke-dasharray="2 3">
    <circle cx="0" cy="0" r="52"/></g>
  <circle cx="0" cy="0" r="44" fill="none" stroke="#9a4234" stroke-width="1.4"/>
  <path id="tnT" d="M0,0 m-34,0 a34,34 0 0,1 68,0" fill="none"/>
  <path id="tnB" d="M0,0 m-34,0 a34,34 0 0,0 68,0" fill="none"/>
  <text font-family="Georgia,serif" font-size="12" letter-spacing="3" fill="#9a4234" font-weight="700">
    <textPath href="#tnT" startOffset="50%" text-anchor="middle">TAINAN</textPath></text>
  <text font-family="Georgia,serif" font-size="9.5" letter-spacing="3" fill="#9a4234">
    <textPath href="#tnB" startOffset="50%" text-anchor="middle">TAIWAN</textPath></text>
  <text x="0" y="-2" text-anchor="middle" font-family="Georgia,serif" font-size="18" font-weight="700" fill="#9a4234">10&#183;11</text>
  <text x="0" y="14" text-anchor="middle" font-family="Georgia,serif" font-size="9" letter-spacing="2" fill="#9a4234">2026</text>
  <path d="M0,-34 l2,5 l5,0 l-4,3 l2,5 l-5,-3 l-5,3 l2,-5 l-4,-3 l5,0 Z" fill="#9a4234"/>
</g>
</svg>'''

with open("assets/frame.svg","w",encoding="utf-8") as f:
    f.write(SVG)
print("svg written", len(SVG))
