# Ces22_ExLab7
Legenda: 
- Qts1 se refere à questão 1. Constam 2 arquivos: 
    - o código em Python exemplificando uma Pizzaria em padrão Decorator
    - a imagem referente ao diagrama de classes dessa Pizzaria
  Não ficou claro no enunciado se era necessário oferecer algum código. Optou-se por fazer leves alterações, apenas a título de exemplificação, no código utilizado em aula para o CoffeeShop, que passou a se referir a uma Pizzaria. Foram mostrados apenas 2 tipos de pizza, mas mais possibilidades podem ser criadas, bem como ingredientes. 
  
  
- Qts2 se refere à questão 2. Constam 2 arquivos:
    -  o código em Python referente a um banco que realiza as operações de verificar saldo, verificar extrado e transferir em padrão Command
    -  a imagem se refere ao diagram de classes desse programa do banco
 
    Houve dúvida na questão 2 se havia necessidade de implementar efetivamente as atividades de verificar saldo, verificar extrado e transferir (ou se poderia-se deixar, por exemplo, apenas um "print"). Por fim, optou-se por implementar as 3 atividades de forma simples, de modo que:
  - verificar saldo apenas retorna o valor de dinheiro em uma determinada conta "Account" (foi-se criada a classe conta, com um atributo "Money")
  - transferir passa um valor determinado de dinheiro de uma conta de origem para uma conta de destino
  - verificar extrato registra os valores transferidos e indica o total de transferências feitas
 Para essa implementação, utilizou-se uma espécie de ferramenta de dicionário, em busca da maior generalidade possível de cabeçalhos, sem perda do padrão Command. O objetivo dessa implementação foi restringir os locais de possibilidade de mudança futura no código, caso esse banco passasee a realizar mais tarefas, por exemplo.
 No entanto, o efeito dessa escolha de implementação no diagrama de classes foi perceptível, visto que o número de atributos ficou bastante reduzido, além de algumas relações que não foram mais estabelecidas em relação ao modelo de diagrama de classes associado ao padrão Command apresentado nos slides da aula 13(pdf e vídeo numerados como 15).
