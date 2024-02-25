### Farben Skript

Alice und Bob wollten Informationen sicher austauschen und wendeten den Diffie-Hellman-Schlüsselaustausch auf der Basis von Farben an. Die folgenden Schritte wurden durchgeführt:

**Auswahl privater Farben:**
Alice wählt Rot als ihre private Farbe.
Bob wählte Blau als seine private Farbe.

**Auswahl einer öffentlichen Farbe:**
Gelb wurde als öffentliche Farbe festgelegt, die für beide Parteien sichtbar ist.

**Individuelle Farbkombinationen:**
Alice multipliziert ihre private Farbe Rot mit der öffentlichen Farbe Gelb und erhält eine Mischfarbe, z.B. Orange.
Bob multipliziert seine private Farbe Blau mit der öffentlichen Farbe Gelb und erhält eine weitere Mischfarbe, z.B. Grün.

**Tauschen und neu kombinieren:**
Die Parteien tauschen ihre privaten Farben, so dass Alice nun Bobs private Farbe Blau besitzt und Bob Alices private Farbe Rot erhält.
Jede Partei kombinierte die erhaltene private Farbe mit ihrer ursprünglichen privaten Farbkombination. Alice kombinierte Orange mit Blau und Bob kombinierte Grün mit Rot.

Dieser Prozess führte zu einer gemeinsamen Mischfarbe, die als Ergebnis des Farbaustauschs und des Diffie-Hellman-Schlüsselaustauschs fungierte. Diese gemeinsame Mischfarbe diente als sicherer Schlüssel, um den Informationsaustausch zwischen Alice und Bob zu schützen.


### Farben Skript
Wir haben wieder Alice und Bob.
Alice ist auf der linken Seite und Bob auf der Rechten.
Dazwischen ist die Öffentlichkeit bzw. ein Dritter.


Schauen wir uns nun die Funktionsweise des Diffie-Hellman Key-Exchange Alogrithmus anhand von Farben an.

**Auswahl privater Farben:**
Alice wählt eine random Farbe aus, die nur sie alleine kennt. In diesem fall die Farbe Rot. Wir nennen die Farbe mal a.

Das gleiche macht auch Bob.
Er wählt auch eine Farbe, die nur er alleine kennt. In diesem Fall die Farbe Blau. Diese nennen wir b.

Dann einigen sie sich beide auf eine Zahl n und eine Generatorfarbe g. In diesem Fall Gelb. Diese ist der Öffentlichkeit bekannt.

Nun nimmt Alice ihre geheime Farbe und vermischt sie mit der öffentlichen Farbe. Dadurch erhält sie eine neue Farbe ag, die Orange ist. Diese wird sie später öffentlich mit Bob teilen.

Das gleiche macht auch Bob.
Er mischt seine private Farbe mit der öffentlichen Farbe g und erhält dadurch eine Farbmischung bg. In diesem Fall Grün.

Nun teilt Bob seine öffentliche Farbe bg mit Alice, die diese mit ihrer privaten Farbe vermischt. Dadurch erhält sie die Farbmischung abg.

Auch Alice teilt ihre öffentliche Farbe ag mit Bob, der diese mit seiner privaten Farbe vermischt. Dadurch erhält er auch die Farbmischung abg

Beide kriegen am Ende die gleiche Farbe heraus und haben somit ein shared secret oder auch Key genannt. Wenn ein Dritter nun versucht die öffentlichen Farben zu mischen wird er nicht die gleiche Farbe wie Alice und Bob herausbekommen können, ohne deren geheime Farben zu kennen. Und so funktioniert der Diffie-Hellman Key-Exchange Alogrithmus.

Schauen wir uns das ganze mal aus der Mathematischen Perspektive an.