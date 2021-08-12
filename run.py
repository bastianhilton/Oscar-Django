from waitress import serve
import shop

serve(shop, listen='*:8001')