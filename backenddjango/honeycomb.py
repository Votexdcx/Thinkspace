import os
from opentelemetry import trace
from opentelemetry.instrumentation.django import DjangoInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

os.environ.setdefault("OTEL_EXPORTER_OTLP_ENDPOINT", "https://api.honeycomb.io")
os.environ.setdefault("OTEL_EXPORTER_OTLP_HEADERS", " x-honeycomb-team=lYrlcTiSSyT9iBYF2K1FgC")
os.environ.setdefault("OTEL_SERVICE_NAME", "ThinkSpace")


# Resource info
resource = Resource.create({
    "service.name": os.environ.get("OTEL_SERVICE_NAME", "ThinkSpace"),
})

# Set tracer provider and exporter
provider = TracerProvider(resource=resource)
processor = BatchSpanProcessor(OTLPSpanExporter())
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)

# Set tracer (optional, if you want to add manual spans later)
tracer = trace.get_tracer(__name__)

# Instrument Django and requests
DjangoInstrumentor().instrument()
RequestsInstrumentor().instrument()