### Start

Der Diffie-Hellman Key-Exchange Alogrithmus

Der Algorithmus wird täglich von uns gebraucht, ohne das wir es wissen. Aber um einmal zu verstehen, was der Algorithmus macht und wie er funktioniert wollen wir uns ein Beispiel aus dem Leben anschauen.

Sagen wir es gibt zwei Personen: Alice und Bob.
Beide wollen sich ein Geheimnis austauschen.
Dafür kommen sie nahe zu einander uns flüsstern sich das Geheimniss zu.

Im echten Leben funktioniert das sehr gut.
Aber was ist, wenn Alice und Bob sich nicht in Person treffen können und über das Internet miteinander komunizieren.
Hier können sie sich nicht einfach etwas zu flüstern.

Sagen wir Alice und Bob schreiben über das internet miteinander.
Es gibt aber noch eine Dritte Person, die die Nachrichten abfängt und liest.
Das wollen Alice und Bob natürlich verhindern.
Aber wie können sie das machen?

An dieser Stelle setzt der Diffie-Hellman Key-Exchange Alogrithmus ein.
Dieser verschlüsselt die Nachricht mit einem Key.
Nur wer den Key kennt, kann die Nachricht lesen und verstehen.
Dadurch kann der Dritte sich keinen Zugang mehr zu den Geheimnissen von Alice und Bob verschaffen.

Aber wie funktioniert der Diffie-Hellman Key-Exchange Alogrithmus?

Dafür werden wir uns das Beispiel von grade einmal mit Farben angucken.

Der Algorithmus basiert auf einem Schlüssel.
Dafür müssen sowohl Alice als auch Bob sich eine Farbe ausdenken, die nur sie selbst wissen. D.h sie teilen diese Farben nicht miteinander.

Dann wird noch eine random Zahl generiert und eine Farbe. Diese sind öffentlich und für alle zugeänglich.

Alice mischt ihr Farbe dann mit der öffentlichen Farbe und erhällt dadurch eine neue Farbe.

Das gleiche macht Bob auch.

Danach teile sie ihre neuen Farben miteinander.

Daraufhin mischt Alice die Farbmischung von Bob mit ihrer geheimen Farbe. Daraufhin erhälte sie die Finale Farbe.

Das gleiche macht auch Bob. Er mischt die Farbe von Alice mit seiner geheimen Farbe.

Das Resultat ist, dass beide bei der gleichen Farbe rauskommen.
Das sogenannte shared secret. Mithilfe von diesem Schlüssel können sie nun Geheim daten austauschen.

Ein Dritter kennt nur die öffenlichen Farben und kann nicht herausfinden, wie diese zusammengestellt wurden.

Das war eine Veranschaulichung mit Farben.

Jetzt gucken wir uns aber einmal die mathematik dahinter an, und wieso diese Funktioniert.

### Next scene

Auf der Linken seite haben wir wieder Alice und auf der rechten Seite Bob.
Dazwischen ist die öffentlichkeit bzw. ein Dritter.

Alice überlegt sich eine Zahl a und Bob eine Zahl b.
Diese Zahl bleibt geheim und nur sie selbst kennen sie.

Dann wird ein Generator g und eine Zahl n für beide ausgewählt, die der Öffentlichkeit bekannt sind.

Daraufhin berechnet Alice nach der Formel g^n mod n ihre öffentliche Zahl.
Das gleich macht Bob auch.

Bob teil dann seine öffentliche Zahl mit Alice, die dann die Zahl von Bob mit ihrer privaten Zahl verrechnet und mod n nimmt.

Das selbe gilt für Bob

Die gleiche rechnung können wir auch mit g^ba mod n darstellen.
Bei Bob ist es dann g^ab mod n.

Hier stehen die gleichen Rechnungen da hier die produktregel angewendet werden kann.


Das Ergebniss ist, dass Alice und Bob die Gleiche Zahl und somit den gleichen Key rausbekommen.
Der öffenlichkeit ist es aber nicht möglich, die Zahl auszurechnen, wodurch der Key geheim bleibt, obwohl Teile von ihm öffentlich geteilt wurden.

### Next scene

Gehen wir das den Algorithmus mal mit konkreten Zahlen durch.

Sagen wir a entspricht 10
g ist 3
n=17

Dann müssen wir die Zahlen nur noch in die Formel g^a mod n einsetzen.
Das entspricht der Zahl 5





