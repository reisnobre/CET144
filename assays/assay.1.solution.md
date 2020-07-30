# Prova

## 1. SATISFIABILITY

Satisfiability, também chamado de SAT, trata-se de um problema da lógica e ciência da computação que busca determinar a se existe uma interpretação que satisfaça uma data formula Booleana.

Em outras palavras busca responder se as variáveis de uma dada formula Booleana podem ser consistentemente substituídas por valores TRUE e FALSE de maneira a gerar um resultado TRUE. Se sim a formula em questão é chamada **satisfiable**.

SAT foi o primeiro problema a ser provado com **NP-COMPLETO** isso significa que o problema se encontra numa categoria de problemas de otimização que por definição não podem ser resolvidos de forma eficiente e se acredita que não existem algoritmos para solucionar problemas pertencentes a essa classe.

Entretanto, em 2007, algoritmos utilizando heurísticas de inteligência artificial mostraram se capazes de resolver instância desses problemas contendo dezenas de milhares variáveis e milhões de símbolos, o que é suficiente para diversos casos.

Existem alguns algoritmos de alto desempenho que resolvem instâncias do problema SAT, são evoluções do Algoritmo DPLL (Davis-Putnam-Logemann-Loveland). Esses algoritmos são baseados em backtracking para decidir a satisfazibilidade das fórmulas de lógica.  Algoritmos genéticos estão sendo usados para resolver problemas SAT, com certas restrições, onde não há conhecimento da limitado da estrutura específica das instâncias do problema. Utilizando redes neurais, o problema poderia ser resolvido devido ao fato de que o algoritmo de redes neurais iria ser treinado para encontrar uma solução ótima, utilizando back propagation. As heurísticas de colônia de formigas também podem resolver o problema do SAT, isso porque, esse tipo de algoritmo resolve problema que envolvem a procura de caminhos em grafos.

## Diferentes implementações para o artigo: Ant colony optimization for real world vehicle routing problems

### Redes Neurais Artificiais (ANN)

Redes Neurais Artificiais são técnicas computacionais representar através de um modelo matemático o processo de aprendizado realizado por um cérebro, adquirindo conhecimento através da experiências passadas. Uma grande ANN pode ter centenas ou milhares de unidades de processamento chamadas de perceptrons, que buscam modelar o funcionamento de neurônios orgânicos.

Essas unidades, geralmente são conectadas por canais de comunicação que estão associados a determinado peso. As unidades fazem operações apenas sobre seus dados locais, que são entradas recebidas pelas suas conexões. O comportamento inteligente de uma ANN vem das interações entre as unidades de processamento da rede.

O Problema de Roteirização de Veículos (PRV) é de grande importância para o gerenciamento das atividades de coleta e distribuição de cargas, por se tratar de um problema de grande importância, se tornou um dos mais estudados. Para o problema PRV para se adequar a uma ANN é recebido com entrada uma frota de veículo localizados no depósito onde cada veículo possui a mesma capacidade. Também são definidas as localizações das cidades e suas respectivas demandas. O objetivo é que cada veículo é encontrar uma rota que começa no depósito, visita um subconjunto de cidades e retorna ao depósito sem violar a restrição de capacidade definida.

O objetivo é definir quais cidades serão visitadas por um veículo específico. Os neurônios podem ser inicializados a partir de um cálculo contendo a razão entre a capacidade dos veículos, a localização das cidades e a demanda das mesmas. A taxa de aprendizagem pode ser definida na implementação assim como pode ser escolhido um critério de parada.

A função de ativação pode ser definida para se obter a menor distância Euclidiana do peso do nó com o vetor de entrada de pesos. O algoritmo pode ser finalizado quando o erro mínimo desejável é alcançado ou o valor mínimo para a taxa de aprendizagem é observado.

Em resumo, no algoritmo observa-se uma competição entre os neurônios da camada de saída, resultando em um neurônio vencedor que atenda ao critério estabelecido, que em geral é a distância Euclidiana. Em seguida, observa-se uma fase cooperativa entre os neurônios, quando é definida a vizinhança do neurônio vencedor. Por fim, os pesos do neurônio vencedor e de sua vizinhança são ajustados, caracterizando esta fase final como adaptativa. Também é observado o padrão dos neurônios de entrada e os respectivos pesos de seus neurônios vencedores.

### Algoritmos Genéticos

Heurística que busca simular o processo de seleção natural. O algoritmo consiste em criar uma população de possíveis soluções para um dado problema, diferentes variações do mesmo permitem que soluções impossíveis. Após inicializar a população, através de uma função de cruzamento são gerados novos indivíduos, contendo partes da solução de cada um dos seus progenitores, uma taxa de mutação pode ser implementada para introduzir uma certa variação que é necessária para uma solução equilibrada.

Os indivíduos escolhidos são através de uma medida de fitness, que para o problema de rotas de veículos, podem ser os mesmos utilizados na solução original, uma combinação de tempo, distância e % de entregas realizadas.

Após o processo de cruzamento, pode se “mata” todos os progenitores ou manter os progenitores que tem uma medida de fitness acima de um certo valor.
Para cada indivíduo, os seus genes representaram uma possível combinação de pontos e entrega. No processo de cruzamento, partes da rota dos progenitores A e partes da rota do progenitor B serão combinadas para criar o indivíduo C.

### Colônia de Formigas (ACO)

O algoritmo colônia de formigas é muito utilizado para traçar uma rota eficiente, de modo que seja o melhor caminho, em problemas de grafo. O algoritmo consiste numa heurística que visa simplificar questões complexas e ocorre de forma intuitiva fundamentado em experiências, baseado em probabilidade.

A heurística aqui utilizada se faz bastante útil para esse tipo de situação, visto que o problema lida com o objetivo optimizar rotas buscando reduzir os custos de transporte. Pode-se então traçar um grafo para representar uma data rota e utilizar o ACO percorrer diversas rotas e assim encontrar uma possibilidade de caminho ótimo.

No algoritmo, deve-se escolher o lugar que será a colônia e a partir dai realizar os testes. Após essa escolha, os veículos entraram em trânsito por possíveis rotas para a entrega. O algoritmo deve analisar e verificar quais rotas, pelo processo de distribuição e evaporação de feromônios a rota que tem a maior probabilidade  de ser boa, pois será por ela que os caminhões chegam mais rápido tanto no ponto de partida quanto o de chegada, realizando o reforço da dada rota.
jk