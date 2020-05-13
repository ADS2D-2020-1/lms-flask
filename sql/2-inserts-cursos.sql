INSERT INTO cursos (nome, sigla, tipo, coordenador, duracao, matutino, noturno)
VALUES ('Análise e Desenvolvimento de Sistemas', 'ADS', 'Tecnólogo', 'Ana Cristina dos Santos', 5, 1, 1);
UPDATE cursos 
   SET sobre = '<p>
                O curso de Análise e Desenvolvimento de Sistemas da Faculdade Impacta foi 
                reconhecido pelo ENADE/MEC como um dos melhores da cidade de São Paulo.
              </p>
              <p>
                Com a transformação digital e a área de tecnologia sempre em alta, o 
                curso forma um profissional que possa se envolver em todas as etapas
                do projeto de sistemas de software, desde concepção, análise, projeto,
                teste, gestão, implantação e manutenção de sistemas de informação.
              </p>
              <p>
                Atualmente, as carreiras mais demandadas pelo mercado de trabalho são 
                para desenvolvedor web, mobile e a Internet das Coisas (IoT), além de 
                profissionais com conhecimento em DevOps (Ambiente de Operação e Desenvolvimento).
              </p>
              <p>
                O profissional de DevOps precisa ter habilidades para fundir desenvolvimento e 
                implantação de aplicativos em um processo automatizado, de entrega contínua, em
                que as responsabilidades são compartilhadas entre equipe de operação e equipe 
                de desenvolvimento, facilitando o desenvolvimento, integração, entrega, processos de
                monitoramento contínuos de software e a gestão da infraestrutura de TI.
              </p>
              <p>
                Para o trabalho do profissional de desenvolvimento web, mobile e IOT, aprende-se a 
                programar em linguagens de programação ou marcação, tais como: HTML, CSS, 
                Javascript e Python, assim como frameworks relacionados e banco de dados com SQL, 
                para criação de aplicativos para sites, aplicativos móveis e IoT.
              </p>
              <p>
                Os desenvolvedores precisam ainda entender os requisitos de negócio do cliente e fornecer
                recomendações para melhorar os aplicativos ou sistemas de software, a fim de garantir que
                atendam às necessidades dos usuários ou clientes.
              </p>
              <p>
                Esses diferenciais na formação de habilidades e competências do nosso curso permitem aos
                 alunos trabalharem em empresas das mais variadas áreas de aplicações, ocupando carreiras 
                 como de analista de sistemas, analista de requisitos, analista de negócio, desenvolvedor 
                 web, mobile ou IoT e DevOps, analista de teste e gerente de projeto.
              </p>'
 WHERE sigla = 'ADS';

INSERT INTO cursos (nome, sigla, tipo, coordenador, duracao, matutino, noturno)
VALUES ('Sistemas da Informação', 'SI', 'Bacharelado', 'Osvaldo Kotaro Takai', 8, 1, 1);

UPDATE cursos
   SET sobre = '<p>
                A graduação de Sistemas de Informação visa formar empreendedores,
                profissionais e pesquisadores focados na construção, manutenção 
                e evolução dos sistemas computacionais de apoio às organizações.
              </p>
              <p>
                O perfil empreendedor é alcançado a partir da criação de startups 
                e produtos inovadores durante os quatro semestres finais do curso.
              </p>
              <p>
                Já o perfil profissional é alcançado a partir da capacidade de 
                entender e analisar problemas reais e desenvolver soluções pragmáticas 
                com o uso de tecnologias de melhor custo-benefício.
              </p>
              <p>
                O constante envolvimento do aluno na solução de problemas impulsiona 
                o perfil investigativo, não apenas como um pesquisador intuitivo, mas, 
                sobretudo, como conhecedor de processos e métodos para a realização de 
                pesquisas científicas.
              </p>
              <p>
                O grande diferencial deste curso está na estrutura curricular: nos 
                quatro primeiros semestres o aluno aprende a <em>"saber fazer"</em>, ou seja,
                o aluno aprende a analisar problemas e criar soluções com o uso das 
                tecnologias da informação. Isso permite que ele receba no meio da graduação 
                o diploma de Análise e Desenvolvimento de Sistemas.
              </p>
              <p>
                Nos quatro semestres finais, o aluno aprende a <em><strong>"inovar"</strong></em>, ou seja, 
                aprende a utilizar a sua capacidade de <em>"saber fazer"</em> para construir produtos 
                ou serviços evolucionários, revolucionários, ou até, disruptivos dentro de 
                suas próprias startups.
              </p>'
 WHERE sigla = 'SI';

INSERT INTO cursos (nome, sigla, tipo, coordenador, duracao, matutino, noturno)
VALUES ('Administração', 'ADM', 'Bacharelado', 'Francesca Romanelli', 8, 0, 1);

UPDATE cursos
   SET sobre = '<p>
                Tornar-se um líder. Ser um empreendedor. Fazer investimentos.
                Você tem inúmeras possibilidades na graduação em Administração
                da Faculdade Impacta.
              </p>
              <p>
                O curso é voltado para as exigências do mercado de trabalho atual 
                e aborda de forma ampla o universo corporativo. Você vai aprender 
                a definir as melhores estratégias para o bom funcionamento das empresas, 
                para gerar lucros, controlar gastos e se destacar com qualidade entre 
                as concorrentes.
              </p>
              <p>
                Gerir equipes, negociar com fornecedores, solucionar diferentes problemas, 
                atingir resultados positivos, aumentar a produtividade e aplicar novas 
                tecnologias nas organizações também são funções do administrador.
              </p>'
 WHERE sigla = 'ADM';


INSERT INTO cursos (nome, sigla, tipo, coordenador, duracao, matutino, noturno)
VALUES ('Redes de Computadores', 'RC', 'Tecnólogo', 'Bruno Luis Soares de Lima', 4, 0, 1);

UPDATE cursos
   SET sobre = '<p>
                Com o advento da Indústria 4.0 e da Internet das Coisas, os sistemas de
                computação são, cada vez mais, dependentes de infraestrutura de redes 
                de comunição, e demandam das mesmas maior desempenho, confiabilidade e segurança.
              </p>
              <p>
                Neste contexto, as empresas dos mais variados setores da economia possuem 
                dependência das redes de computadores no mesmo nível que de energia elétrica.
                Serviços do dia a dia, essenciais para sociedade, dependem de diferentes 
                tipos de redes, como Wi-Fi, intranet, dispositivos móveis conectados, entre outros.
              </p>
              <p>
                O profissional formado pelo curso Superior em Tecnologia em Redes de Computadores 
                estará preparado para atuar neste contexto, analisando, projetando, implementando 
                e administrando soluções para garantir o funcionamento e meio de infraestrutura 
                de tecnologia da informação para diversas aplicações, desde vídeos on demand até 
                aplicações financeiras.
              </p>
              <p>
                O aluno dominará ferramentas e tecnologias voltadas para controles de tráfego, 
                cyber security, dimensionamento da capacidade computacional e implementação de 
                ambientes de execução de aplicações em nuvem, políticas de segurança de informação,
                conectividade e implementação de redes locais e de longa distância.
              </p>
              <p>
                O aluno terá ainda uma visão abrangente da área, com a possibilidade de desenvolver 
                projetos, realizar atividades em laboratório e se preparar para certificações da Cisco,
                que possuem peso e reconhecimento internacional.
              </p>'
 WHERE sigla = 'RC';