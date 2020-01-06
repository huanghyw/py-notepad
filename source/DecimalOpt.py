from decimal import Decimal
from decimal import localcontext, getcontext

a = Decimal(12.345)
b = Decimal(1.000)

print("=" * 100)

print(a * b)
with localcontext() as ctx:
    ctx.prec = 10
    print(a * b)
print(a * b)

print("=" * 100)

print(a.quantize(Decimal('0.01'), rounding="ROUND_CEILING"))
print(a.quantize(Decimal('0.01'), rounding="ROUND_DOWN"))
print(a.quantize(Decimal('0.01'), rounding="ROUND_FLOOR"))
print(a.quantize(Decimal('0.01'), rounding="ROUND_HALF_DOWN"))
print(a.quantize(Decimal('0.01'), rounding="ROUND_HALF_EVEN"))
print(a.quantize(Decimal('0.01'), rounding="ROUND_HALF_UP"))
print(a.quantize(Decimal('0.01'), rounding="ROUND_UP"))
print(a.quantize(Decimal('0.01'), rounding="ROUND_05UP"))

print("=" * 100)

g_ctx = getcontext()
g_ctx.rounding = "ROUND_CEILING"
print(g_ctx.quantize(a * b, Decimal('0.001')))
with localcontext() as ctx:
    ctx.prec = 10
    ctx.rounding = "ROUND_DOWN"
    print((a * b).quantize(Decimal('0.001')))
print(g_ctx.quantize(a * b, Decimal('0.001')))

print("=" * 100)
