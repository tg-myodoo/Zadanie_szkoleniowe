# Zadanie_szkoleniowe
Zadanie szkoleniowe - nowy model: Investor Report

Polecenia:

1. Zbudowanie szkieletu modułu z pierwszymi polami i prostymi metodami.
    - Utworzenie nowego pola "inwestor" w modelu sale.order, widoczne w form view ów modelu (może być pod polem "klient"). Inwestor ma być polem Many2one, powiązanym z res.partner. Te pole nie musi posiadać żadnych właściwości.
    - Utworzenie nowego pola w modelu res.partner "Inwestycje", które będzie polem One2many i będzie ono pobierać info dzięki polu "Inwestor" z sale.order, co znaczy, będzie przechowywac listę SO, w których dany kontakt został wybrany jako inwestor. Pole ma posiadać właściwość readonly, ma być widoczne tylko dla użytkowników z najwyższym uprawnieniem dla modelu Sales, oraz ma wyświetlać numer SO, datę zamówienia / zatwierdzenia, oraz kwoty netto oraz brutto.
    - Utworzenie nowego pola w modelu res.partner "Suma inwestycji", które będzie polem typu Float oraz będzie posiadać uzupełniane za pomocą metody z dekoratorem compute. Metoda ta ma zebrać wszystkie inwestycje danego partnera, zsumować ich wartość netto i wstawić otrzymaną wartość do pola.

2. Rozbudowa metod wraz z dodatkowymi ograniczeniami.
    - Pole zawierające listę SO (Sale Orders) (widok partnera) powinno zawierać tylko te SO, które po pierwsze, należą do danego partnera (już zrobione), oraz, które są w statusie "confirmed", tzn. nie wyświetlaj tych SO, które są w statusie projektu (quotation) lub canceled.
    - Analogicznie, suma inwestycji ma być brana tylko z potwierdzonych SO.
    - Dodaj metodę z dekoratorem constrains, która będzie sprawdzała inwestora którego wybierasz w SO. Jej celem jest uniemożliwienie wybrania tego samego inwestora, który jest jednocześnie klientem dla danego SO, poprzez wywalenie komunikatu UserError. Treść komunikatu dowolna.

3. Stworzenie kompletnie nowego modelu, dzięki któremu możemy tworzyć raporty okresowe oraz je drukować jako PDF.
    - Stwórz zupełnie nowy model (w tym samym module), możesz nazwać InvestorReport, ale w gruncie rzeczy jest to obojętne. Do tego modułu trzeba się dostać drogą Sales --> Reporting (u góry z rozwijanego menu ma być nowa opcja).
    - Model ten ma zawierać pola z nazwą, partnerem (many2one), datą początkową, datą końcową (obie daty mają być Date, nie Datetime), One2many do sale.order, suma netto i suma brutto.
    - Po wybraniu partnera oraz dat, tabela z sale.order one2many ma automatycznie się uzupełnić, czyli mają zostać wybrane te SO w których wybrany partner jest inwestorem, są potwierdzone oraz Order Date mieści się w ramach wybranych przez użytkownika dat.
    - Dodanie możliwości wydrukowania raportu PDF ze wszystkimi informacjami widocznymi w raporcie z form view.
