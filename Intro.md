### Start

Der Diffie-Hellman Key-Exchange Alogrithmus.

Dieser Algorithmus wird täglich von uns gebraucht, ohne das wir es wissen. Er wurde 1976 von Whitfield Diffie und Martin Hellman entwickelt und unter der Bezeichnung ax1x2 veröffentlicht. Es handelt sich hierbei um einen Algorithmus für die Kryptographie.

Aber wofür braucht man den Diffie-Hellman Key-Exchange Alogrithmus und was macht er? Dafür schauen wir uns mal ein Beispiel aus dem Leben an.

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
Dieser verschlüsselt die Nachricht mit einem Key als Schlüssel.
Nur wer den Key kennt, kann die Nachricht lesen und verstehen.
Dadurch kann der Dritte sich keinen Zugang mehr zu den Geheimnissen von Alice und Bob verschaffen.

Aber wie funktioniert der Diffie-Hellman Key-Exchange Alogrithmus?

Dafür werden wir uns ein Beispiel mit Farben anschauen.

1:30 min

## next Scene

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

Dann einigen sich beide auf einen Generator g und eine Zahl n, die der Öffentlichkeit bekannt sind.

Nun kann Alice ihr öffentliche Zahl nach der Formel g^a mod n berechnen.
Das gleich macht Bob auch.

Daraufhin teilt Bob seine öffentliche Zahl mit Alice, die diese Zahl hoch ihrer privaten Zahl a nimmt und modulo n rechnet.

Das selbe gilt für Bob

Nun steht auf der Linken seite das gleiche, wie auf der rechten Seite.

<!-- Die gleiche rechnung können wir auch mit g^ba mod n darstellen.
Bei Bob ist es dann g^ab mod n.

Hier stehen die gleichen Rechnungen da hier die produktregel angewendet werden kann. -->
Somit können wir auf beiden seiten g^ab mod n hinschreiben.

### Next scene

Gehen wir nun den Algorithmus mal mit konkreten Zahlen durch.
So wie vorher ist Alice links und Bob rechts.

Sagen wir a entspricht der Zahl 10, g der Zahl 3, n der Zahl 17 und b der Zahl 5. 
G ist in der Regel eine kleine Primzahl und n eine große Zahl aufgrund der Sicherheit des Algorithmus. N ist normalerweise 2000 - 4000 bits lang. Aber in diesem Beispiel wollen wir die Zahlen einfach halten.

Wenn wir nun wieder die Formel von vorher nehmen und die Werte der Variablen einsetzen kommen wir auf das Ergebnis 8.

Das gleiche machen wir auch bei Bob.
Hier bekommen wir die Zahl 5 raus.


Nun teilt Alice ihre Zahl 8 mit Bob, wodurch sie der öffentlichkeit bekannt wird. Bob kann dann die Zahl in die Formel einsetzen.

Auch Bob teilt seine Zahl 5 mit Alice, die dann auch der öffentlichkeit bekannt ist. Auch Alice setzt die Zahl in die Formel ein.
Sie erhält als Ergebnis 9.

Auch Bob erhält das Ergebnis 9, welches das shared secret darstellt.
Wie vorher dargestellt bekommen sie das gleiche Ergebnis, da die Exponenten beliebig miteinander vertauscht werden können.

Wenn nun die Öffentlichkeit versucht, mit den bekannten Zahlen das secret zu errechnen, wird eine andere Zahl herauskommen.







g ist in der Regel eine kleine Primzahl
n ist oft eine große Zahl aufgrund der Sicherheit des Algorithmus
N ist normalerweise 2000- 4000 bits lang.
Wenn die Zahl zu groß wird gewinnt man nichts mehr an sicherheit aber verliert effizienz.
a ist zwischen 1 und n
