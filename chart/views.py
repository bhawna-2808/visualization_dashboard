from django.shortcuts import render, HttpResponse
from .models import Insight
from rest_framework.views import APIView
from .serializer import *
from rest_framework.response import Response
from rest_framework import status
from django.template.loader import render_to_string
from django.http import JsonResponse


""" This function is used for dashboard and draw all charts as per data. """
def dashboard(request):
    try:
        insights = Insight.objects.all()

        # Data preparation for line chart (e.g., intensity over time)
        line_chart_data = {
            'labels': [],
            'datasets': [{
                'label': 'Intensity',
                'data': [],
                'backgroundColor': 'rgba(75, 192, 192, 0.2)',
                'borderColor': 'rgba(75, 192, 192, 1)',
                'borderWidth': 1,
                'fill': 0  
            }]
        }
        # Data preparation for area chart (e.g., intensity by category)
        area_chart_data = {
            'labels': [],
            'datasets': [{
                'label': 'Intensity',
                'data': [],
                'backgroundColor': 'rgba(75, 192, 192, 0.2)',  # Fill color
                'borderColor': 'rgba(75, 192, 192, 1)',
                'borderWidth': 1
            }]
        }

        # Data preparation for bar chart (e.g., intensity by topic)
        bar_chart_data = {
            'labels': [],
            'datasets': [{
                'label': 'Intensity',
                'data': [],
                'backgroundColor': 'rgba(75, 192, 192, 0.2)',
                'borderColor': 'rgba(75, 192, 192, 1)',
                'borderWidth': 1
            }]
        }

        # Data preparation for pie chart and doughnut chart (e.g., intensity by sector)
        pie_chart_data = []
        doughnut_chart_data = []

        sector_intensity = {}  # To aggregate intensity by sector for pie and doughnut charts

        for insight in insights:
            # Data for line chart
            line_chart_data['labels'].append(insight.published.year)
            line_chart_data['datasets'][0]['data'].append(insight.intensity)

            # Data for bar chart
            bar_chart_data['labels'].append(insight.topic)
            bar_chart_data['datasets'][0]['data'].append(insight.intensity)
            
            
            area_chart_data['labels'].append(insight.topic)
            area_chart_data['datasets'][0]['data'].append(insight.intensity)

            # Data for pie and doughnut charts
            sector = insight.sector
            if sector in sector_intensity:
                sector_intensity[sector] += insight.intensity
            else:
                sector_intensity[sector] = insight.intensity

        # Convert sector_intensity dictionary to list of dictionaries for pie and doughnut charts
        for sector, intensity in sector_intensity.items():
            pie_chart_data.append({
                'label': sector,
                'data': intensity
            })
            doughnut_chart_data.append({
                'label': sector,
                'data': intensity
            })

        return render(request, "pages/dashboard.html", {
            'line_chart_data': line_chart_data,
            'bar_chart_data': bar_chart_data,
            'pie_chart_data': pie_chart_data,
            'doughnut_chart_data': doughnut_chart_data,
            'area_chart_data':area_chart_data
        })
    except Exception as e:
        return render(request, "pages/dashboard.html")


""" This function is used to get data from our insight  models. """
class InsightAPIView(APIView):
    def get(self, request, *args, **kwargs):
        """List insight data """
        try:
            insight_data = Insight.objects.all()
            serializer = InsightModelSerializer(insight_data, many=True)
            return Response(
                {"status_code": status.HTTP_200_OK, "result": serializer.data}
            )
        except Exception as ex:
            print("Error in insight data listing get method", ex)
            return Response(
                {"status_code": status.HTTP_400_BAD_REQUEST, "result": "bad request"}
            )
  
            
""" This function is used for dashboard to view filter functionality. """
def filterinsightdata(request):
    insight_data = Insight.objects.all()
    context = {
        "insight_data": insight_data,
    }

    return render(request, 'pages/filterdata.html', context)
 
 
""" This function is used for dashboard to filter data as per search input.."""                
def datafilterinsightdata(request):
    search_data = request.POST.get('search_input')
    print(search_data)   
    # Perform filtering based on the search text
    filtered_data = Insight.objects.filter(title__icontains=search_data).values(
    'end_year',
    'sector',
    'topic',
    'region',
    'country',
    'pestle',
    'source',
)
    print(filtered_data)
    # Render the filtered data as HTML
    context = {'insight_data': filtered_data}
    html = render_to_string("pages/tabledata.html",context)
    return JsonResponse({"update": html})

