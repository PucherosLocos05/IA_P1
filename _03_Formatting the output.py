# Jesus Antonio Baez Ortega 23310372 6E
# LAB#3 Formatting the output

# Dibuja la figura línea por línea (tradicional)
print("    *")
# ... (resto de líneas)

# Versión optimizada: Usa '\n' para saltos y '*' para repetir líneas idénticas
# El '+ (" * *\n"*2)' ahorra escribir la misma línea del tronco dos veces.
print("    *\n" "   * *\n" + ("  * *\n"*2) + "  *****")

# Versión duplicada: Multiplica cada sección por 2 para mostrar dos figuras paralelas
print(("    * "*2) + "\n" + ("   * * ")*2)