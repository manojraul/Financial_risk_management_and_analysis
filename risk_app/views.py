from django.shortcuts import render
from .utils import analyze_risk

NSE_TICKERS = {
    "TCS": "TCS.NS",
    "Infosys": "INFY.NS",
    "Reliance": "RELIANCE.NS",
    "HDFC Bank": "HDFCBANK.NS",
    "ICICI Bank": "ICICIBANK.NS"
}

US_TICKERS = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Amazon": "AMZN",
    "Google (Alphabet)": "GOOGL",
    "Tesla": "TSLA",
    "Meta": "META"
}

def home(request):
    show_companies = False
    tickers = {}
    selected_market = None

    if request.method == "POST":
        # Step 1: Market selected
        selected_market = request.POST.get("market")
        if selected_market:
            tickers = NSE_TICKERS if selected_market == "NSE" else US_TICKERS
            show_companies = True

        # Step 2: User selected companies and clicked Analyze
        if "stocks" in request.POST:
            selected_tickers = request.POST.getlist("stocks")
            results, chart = analyze_risk(selected_tickers)
            return render(request, "result.html", {"results": results, "chart": chart})

    return render(request, "index.html", {
        "tickers": tickers,
        "selected_market": selected_market,
        "show_companies": show_companies
    })
