from flask import Flask, render_template
app = Flask(__name__)
testo=["Il Duomo di Milano è la cattedrale simbolo della città, un'imponente struttura gotica costruita tra il XIV e il XIX secolo. La facciata del Duomo è decorata con oltre 3.500 statue in marmo bianco e presenta numerosi dettagli architettonici come guglie, pinnacoli e rosoni. All'interno del Duomo si trovano importanti opere d'arte come il presbiterio in marmo di Carrara e la celebre statua dorata della Madonna.<br>La costruzione del Duomo iniziò nel 1386, su progetto di diversi architetti tra cui Simone da Orsenigo e Francesco di Giorgio Martini. Nel corso dei secoli la cattedrale subì numerosi interventi architettonici e decorativi, tra cui la costruzione delle torri nel XVIII secolo e la realizzazione delle vetrate policrome della facciata nel XIX secolo.<br>Oggi il Duomo è uno dei principali simboli della città di Milano, con la sua spettacolare facciata in marmo bianco e la sua terrazza panoramica che offre una vista mozzafiato sulla città.","Il Castello Sforzesco è un'imponente fortezza medievale costruita nel XV secolo per volontà di Francesco Sforza, signore di Milano. La struttura si sviluppa su una superficie di oltre 17.000 metri quadrati e presenta un'ampia corte interna circondata da torri e bastioni. Nel corso dei secoli il Castello subì numerose trasformazioni e venne utilizzato come residenza dei duchi di Milano, come prigione e come caserma militare.<br>Oggi il Castello Sforzesco ospita numerosi musei tra cui la Pinacoteca del Castello Sforzesco, che raccoglie opere di artisti rinascimentali come Leonardo da Vinci e Michelangelo, il Museo d'Arte Antica, il Museo degli Strumenti Musicali e il Museo Egizio.<br>Inoltre, all'interno del Castello si trovano anche la Sala delle Asse affrescata da Leonardo da Vinci e il Cortile della Rocchetta, uno dei più suggestivi della fortezza.","L'Accademia di Belle Arti di Brera, conosciuta comunemente come l'Accademia di Brera, è una delle più importanti istituzioni italiane per la formazione artistica e la conservazione del patrimonio culturale. Fondata nel 1776 dal governo austriaco, l'Accademia di Brera è situata nel cuore del quartiere Brera di Milano e rappresenta un importante centro di studi artistici e culturali.<br>L'Accademia di Brera ospita numerose collezioni d'arte, tra cui dipinti, sculture, disegni e fotografie, conservate all'interno di una serie di gallerie e musei. La collezione permanente dell'Accademia di Brera è composta da oltre 1800 opere d'arte, tra cui dipinti di grandi maestri italiani come Raffaello, Caravaggio, Mantegna, Tintoretto e Canaletto.<br>Inoltre, l'Accademia di Brera offre una vasta gamma di programmi di formazione artistica, tra cui corsi di laurea triennale e magistrale in Belle Arti, Scenografia, Design e Conservazione dei Beni Culturali. Gli studenti dell'Accademia di Brera hanno accesso a laboratori di arte contemporanea, di scultura, di restauro e di fotografia, oltre a workshop e programmi di scambio internazionale.<br>L'Accademia di Brera è anche nota per la sua biblioteca specializzata in storia dell'arte, con oltre 100.000 volumi, tra cui libri antichi, cataloghi d'arte e riviste specializzate. Inoltre, l'Accademia di Brera ospita regolarmente mostre d'arte temporanee, conferenze e altri eventi culturali, che attirano visitatori e appassionati d'arte da tutto il mondo.<br>In sintesi, l'Accademia di Brera rappresenta un importante centro di formazione artistica e di conservazione del patrimonio culturale italiano, che continua a ispirare artisti e appassionati d'arte in tutto il mondo.","La Galleria Vittorio Emanuele II è una delle gallerie commerciali più famose e antiche del mondo, costruita nel XIX secolo in stile neoclassico. La struttura presenta un'ampia vetrata centrale a forma di croce, che la rende particolarmente luminosa e suggestiva. Nella Galleria si trovano numerosi negozi di moda e di lusso, ristoranti e caffè storici come il celebre Camparino.<br>La Galleria è stata progettata dall'architetto Giuseppe Mengoni, che morì durante i lavori di costruzione cadendo dal tetto della struttura. La Galleria Vittorio Emanuele II è anche famosa per la suatradizione che prevede di calpestare con il tallone il mosaico raffigurante il toro presente sul pavimento della galleria. Si dice che questo porti fortuna a chi lo fa e molti visitatori del luogo si concedono questo rito.<br>Galleria Vittorio Emanuele II è anche famosa per la sua architettura e decorazioni, tra cui le statue dei quattro continenti posti alle estremità della galleria, le cupole e le decorazioni in ferro battuto. Inoltre, il salone principale ospita spesso mostre ed eventi culturali e rappresenta uno dei principali luoghi di incontro per i milanesi e i visitatori della città."]
immagine=["static/images/duomo.jpg","static/images/castello.jpg","static/images/brera.jpg","static/images/vittorio.jpg"]
@app.route('/')
def home():
  return render_template("home.html", Titolo='HOME')

@app.route('/immagini')
def hello_world():
  return render_template("immagini.html", Titolo='immagini')
@app.route('/duomo')
def duomo():
  x=0
  return render_template("prova.html", Titolo='prova',testo=testo[x],immages=immagine[x])
@app.route('/castello')
def castello():
  x=1
  return render_template("prova.html", Titolo='prova',testo=testo[x],immages=immagine[x])
@app.route('/brera')
def brera():
  x=2
  return render_template("prova.html", Titolo='prova',testo=testo[x],immages=immagine[x])

@app.route('/vittorio')
def vittorio():
  x=3
  return render_template("prova.html", Titolo='prova',testo=testo[x],immages=immagine[x])
  
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)