#CODIGO ANSI PARA REPRESENTAR CORES NO TERMINAL
#O código ANSI é um padrão para controlar a formatação, cor e estilo do texto em terminais de computador. Ele é amplamente utilizado para adicionar cores e estilos ao texto exibido no terminal, tornando a saída mais visualmente atraente e fácil de ler. O código ANSI é composto por sequências de caracteres que começam com o caractere de escape (ESC) seguido por um código específico para a formatação desejada. Por exemplo, para definir a cor do texto, você pode usar códigos como "\033[31m" para vermelho, "\033[32m" para verde, "\033[33m" para amarelo, e assim por diante. Para resetar a formatação e voltar ao estilo padrão, você pode usar o código "\033[0m". Esses códigos podem ser combinados para criar efeitos mais complexos, como texto em negrito, sublinhado, ou com fundo colorido. O uso do código ANSI é uma maneira eficaz de melhorar a legibilidade e a estética da saída do terminal, especialmente em scripts e programas que geram uma grande quantidade de texto ou que precisam destacar informações importantes.
#Exemplo de uso do código ANSI para colorir o texto no terminal:
print("\033[31mEste texto está em vermelho\033[0m")
print("\033[32mEste texto está em verde\033[0m")
print("\033[33mEste texto está em amarelo\033[0m")
print("\033[34mEste texto está em azul\033[0m")
print("\033[1mEste texto está em negrito\033[0m")
print("\033[4mEste texto está sublinhado\033[0m")
#cores de fundo
print("\033[41mEste texto tem fundo vermelho\033[0m")
print("\033[42mEste texto tem fundo verde\033[0m")
print("\033[43mEste texto tem fundo amarelo\033[0m")
print("\033[44mEste texto tem fundo azul\033[0m")
