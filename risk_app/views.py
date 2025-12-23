from django.shortcuts import render
from .utils import analyze_risk

def home(request):
    if request.method == "POST":
        stocks = request.POST.get("stocks")
        stock_list = [s.strip().upper() for s in stocks.split(",")]
        results = analyze_risk(stock_list)
        return render(request, "result.html", {"results": results})

    return render(request, "index.html")
