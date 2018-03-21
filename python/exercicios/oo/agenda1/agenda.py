"""
###########################################################
##                                                       ##
##                IFNMG Campus Januária                  ##
##            Projeto Bate-papo Tecnológico              ##
##              Python Orientado a Objetos               ##
##          Exercício de Agenda de Contatos OO           ##
##                  Prof. Danilo Nunes                   ##
##              <danilo.nunes@ifnmg.edu.br>              ##
##                                                       ##
###########################################################
"""

__project_name__ = 'Projeto Bate-papo Tecnológico'
__course_name__ = 'Python Orientado a Objetos'
__lesson__ = 'Exercício de Agenda de Contatos OO'
__author__ = 'Prof. Danilo Nunes <danilo.nunes@ifnmg.edu.br>'
__source__ = 'http://github.com/danilonunes/cursos'


ERR_ATTR_INVALID = 'O valor informado para \"{0}\" é inválido.'

from validators import url, domain

class Categoria(object):
    '''
        Classe Categoria:
            Objetivo: definir categorias de endereço, tais como: residencial,
            comercial, praia, campo, etc.
    '''

    def __init__(self, nome):
        '''
            Método de inicialização de uma instância da classe Categoria.
            Recebe como argumento o "nome" que será atribuído a propriedade
            "nome" da instância.
        '''
        self.nome = nome

    @property
    def nome(self):
        '''
            Propriedade (rw) nome: nome de uma categoria de endereço.
        '''
        return self._nome

    @nome.setter
    def nome(self, value):
        if not isinstance(value, str):
            raise Exception(ERR_ATTR_INVALID.format(self.__class__.__name__+'.nome'))

        self._nome = value

    def __repr__(self):
        return '<Categoria nome=%s>' % (self.nome)

class Endereco(object):
    def __init__(self, logradouro, complemento, numero, bairro, cidade, estado,
        pais, cep, categoria):
        '''
            Método de inicialização de uma instância da classe Endereço.
            Recebe como os argumentos "logradouro, complemento, numero, bairro,
            cidade, estado, pais, cep e categoria" que serão atribuído as
            devidas propriedades da instância.
        '''
        self.logradouro = logradouro
        self.complemento = complemento
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.pais = pais
        self.cep = cep
        self.categoria = categoria

    @property
    def logradouro(self):
        '''
            Propriedade (rw) logradouro: logradouro de um endereço.
        '''
        return self._logradouro

    @logradouro.setter
    def logradouro(self, value):
        self._logradouro = str(value)

    @property
    def complemento(self):
        '''
            Propriedade (rw) complemento: complemento de um endereço.
        '''
        return self._complemento

    @complemento.setter
    def complemento(self, value):
        self._complemento = str(value)

    @property
    def numero(self):
        '''
            Propriedade (rw) numero: numero de um endereço.
        '''
        return self._numero

    @numero.setter
    def numero(self, value):
        self._numero = str(value)

    @property
    def bairro(self):
        '''
            Propriedade (rw) bairro: bairro de um endereço.
        '''
        return self._bairro

    @bairro.setter
    def bairro(self, value):
        self._bairro = str(value)

    @property
    def cidade(self):
        '''
            Propriedade (rw) cidade: cidade de um endereço.
        '''
        return self._cidade

    @cidade.setter
    def cidade(self, value):
        self._cidade = str(value)

    @property
    def estado(self):
        '''
            Propriedade (rw) estado: estado de um endereço.
        '''
        return self._estado

    @estado.setter
    def estado(self, value):
        self._estado = str(value)

    @property
    def pais(self):
        '''
            Propriedade (rw) pais: pais de um endereço.
        '''
        return self._pais

    @pais.setter
    def pais(self, value):
        self._pais = str(value)

    @property
    def cep(self):
        '''
            Propriedade (rw) cep: cep de um endereço.
        '''
        return self._cep

    @cep.setter
    def cep(self, value):
        self._cep = str(value)

    @property
    def categoria(self):
        '''
            Propriedade (rw) categoria: categoria de um endereço.
        '''
        return self._categoria

    @categoria.setter
    def categoria(self, value):
        if not isinstance(value, Categoria):
            raise Exception(ERR_ATTR_INVALID.format(
                self.__class__.__name__+'.categoria'))

        self._categoria = value

    def __repr__(self):
        return '<Endereco logradouro=%s, complemento=%s, numero=%s, bairro=%s,'\
            ' cidade=%s, estado=%s, pais=%s, cep=%s, categoria=%s>' % (
            self.logradouro, self.complemento, self.numero, self.bairro,
            self.cidade, self.estado, self.pais, self.cep, self.categoria)

class Tipo(object):
    '''
        Classe Tipo:
            Objetivo: definir tipos de telefones, tais como: residencial,
            celular, etc.
    '''

    def __init__(self, nome):
        self.nome = nome

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        if not isinstance(value, str):
            raise Exception(ERR_ATTR_INVALID.format(self.__class__.__name__+'.nome'))

        self._nome = value

    def __repr__(self):
        return '<Tipo nome=%s>' % (self.nome)

class Telefone(object):

    def __init__(self, ddd, prefixo, sulfixo, ramal, tipo):
        self.ddd = ddd
        self.prefixo = prefixo
        self.sulfixo = sulfixo
        self.ramal = ramal
        self.tipo = tipo

    @property
    def ddd(self):
        return self._ddd

    @ddd.setter
    def ddd(self, value):
        if not isinstance(value, str):
            raise Exception(ERR_ATTR_INVALID.format(self.__class__.__name__+'.ddd'))

        self._ddd = value

    @property
    def prefixo(self):
        return self._prefixo

    @prefixo.setter
    def prefixo(self, value):
        if not isinstance(value, str):
            raise Exception(ERR_ATTR_INVALID.format(self.__class__.__name__+'.prefixo'))

        self._prefixo = value

    @property
    def sulfixo(self):
        return self._sulfixo

    @sulfixo.setter
    def sulfixo(self, value):
        if not isinstance(value, str):
            raise Exception(ERR_ATTR_INVALID.format(self.__class__.__name__+'.sulfixo'))

        self._sulfixo = value

    @property
    def ramal(self):
        return self._ramal

    @ramal.setter
    def ramal(self, value):
        if not isinstance(value, str):
            raise Exception(ERR_ATTR_INVALID.format(self.__class__.__name__+'.ramal'))

        self._ramal = value

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, value):
        if not isinstance(value, Tipo):
            raise Exception(ERR_ATTR_INVALID.format(
                self.__class__.__name__ + '.tipo'))

        self._tipo = value

    def __repr__(self):
        return '<Telefone ddd=%s, prefixo=%s, sulfixo=%s, ramal=%s>' % (
            self.ddd, self.prefixo, self.sulfixo, self.ramal)

class Contato(object):
    def __init__(self, nome, apelido, site=None):
        self._ult_id_telefone = 0
        self._ult_id_endereco = 0
        self.nome = nome
        self.apelido = apelido
        self.site = site
        self._enderecos = {}
        self._telefones = {}

    def _defineIdTelefone(self):
        self._ult_id_telefone += 1
        return self._ult_id_telefone

    def _defineIdEndereco(self):
        self._ult_id_endereco += 1
        return self._ult_id_endereco

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        if not isinstance(value, str):
            raise Exception(ERR_ATTR_INVALID.format(
                self.__class__.__name__ + '.nome'))

        self._nome = value

    @property
    def apelido(self):
        return self._apelido

    @apelido.setter
    def apelido(self, value):
        if not isinstance(value, str):
            raise Exception(ERR_ATTR_INVALID.format(
                self.__class__.__name__ + '.apelido'))

        self._apelido = value

    @property
    def site(self):
        return self._site

    @site.setter
    def site(self, value):
        # verifica se é uma URL ou Domínio válido.
        if not url(value) and not domain(value):
            raise Exception(ERR_ATTR_INVALID.format(
                self.__class__.__name__ + '.site'))

        self._site = value

    @property
    def enderecos(self):
        return self._enderecos

    def setEndereco(self, logradouro, complemento, numero, bairro, cidade,
        estado, pais, cep, categoria):
        e = Endereco(logradouro, complemento, numero, bairro, cidade, estado,
                pais, cep, categoria)

        e_id = self._defineIdEndereco()
        self._enderecos[e_id] = e

    @property
    def telefones(self):
        return self._telefones

    def setTelefone(self, ddd, prefixo, sulfixo, ramal, tipo):
        t = Telefone(ddd, prefixo, sulfixo, ramal, tipo)

        t_id = self._defineIdTelefone()
        self._enderecos[t_id] = t


    def __repr__(self):
        return '<Contato nome=%s, apelido=%s, site=%s, telefones=%s, '\
            'enderecos=%s>' % (self.nome, self.apelido, self.site,
            self.telefones, self.enderecos)

class Agenda1(object):
    def __init__(self):
        self._ult_id_tiposTelefone = 0
        self._ult_id_categoriasEndereco = 0
        self._ult_id_cadastro = 0
        self._tiposTelefone = {}
        self._categoriasEndereco = {}
        self._cadastro = {}

    def _defineIdTipoTelefone(self):
        self._ult_id_tiposTelefone += 1
        return self._ult_id_tiposTelefone

    def _defineIdCategoriaEndereco(self):
        self._ult_id_categoriasEndereco += 1
        return self._ult_id_categoriasEndereco

    def _defineIdCadastro(self):
        self._ult_id_cadastro += 1
        return self._ult_id_cadastro

    def addCategoriaEndereco(self, nome):
        if not isinstance(nome, str):
            raise Exception(ERR_ATTR_INVALID.format('Categoria de endereço'))

        n_id = self._defineIdCategoriaEndereco()
        self._categoriasEndereco[n_id] = Categoria(nome)

    def upgCategoriaEndereco(self, id, nome):
        '''
            Método para atualizar uma categoria de endereço.
        '''
        pass

    def rmCategoriaEndereco(self, id):
        '''
            Método para remover uma categoria de endereço.
        '''
        pass

    def getCategoriasEndereco(self):
        ce = []
        for i in self._categoriasEndereco:
            ce.append(tuple([i, self._categoriasEndereco[i].nome]))

        return tuple(ce)

    def addTipoTelefone(self, nome):
        if not isinstance(nome, str):
            raise Exception(ERR_ATTR_INVALID.format('Tipo de endereço'))

        n_id = self._defineIdTipoTelefone()
        self._tiposTelefone[n_id] = Tipo(nome)

    def upgTipoTelefone(self, id, nome):
        '''
            Método para atualizar um tipo de telefone.
        '''
        pass

    def rmTipoTelefone(self, id):
        '''
            Método para atualizar um tipo de telefone.
        '''
        pass

    def getTiposTelefone(self):
        tt = []
        for i in self._tiposTelefone:
            tt.append(tuple([i, self._tiposTelefone[i].nome]))

        return tuple(tt)

    def addContato(self, nome, apelido, site, enderecos=None, telefones=None):
        '''
            O argumento "enderecos" deve ser informado como uma list com dict(s)
            contendo as seguintes chaves: logradouro, complemento, numero,
            bairro, cidade, estado, pais, cep e categoria.
                Ex.: enderecos=[
                    {'logradouro':'Rua ...', 'complemento': '...',
                    'numero':'...', 'bairro':'...', 'cidade':'...',
                    'estado':'...', 'pais':'Brasil', 'cep':'39480-xxx',
                    'categoria':1},
                    {'logradouro':'Av. ...', 'complemento': '...',
                    'numero':'...', 'bairro':'...', 'cidade':'...',
                    'estado':'...', 'pais':'Brasil', 'cep':'xxxxx-xxx',
                    'categoria':2}
                    ]

            O argumento "telefones" deve ser informado como uma list com dict(s)
            contendo as seguintes chaves: ddd, prefixo, sulfixo, ramal, tipo.
                Ex.: telefones=[
                    {'ddd':'38', 'prefixo':'3629', 'sulfixo':'4600', 'ramal':'',
                    'tipo':1},
                    {'ddd':'38', 'prefixo':'3629', 'sulfixo':'4600', 'ramal':'10',
                    'tipo':2}
                    ]
        '''
        contato = Contato(nome, apelido, site)

        if len(enderecos):
            for e in enderecos:
                if e['categoria'] in self._categoriasEndereco:
                    c = self._categoriasEndereco[e['categoria']]
                else:
                    raise Exception('A categoria de endereço \'{0}\' não foi '\
                        'encontrada'.format(e['categoria']))

                contato.setEndereco(e['logradouro'], e['complemento'],
                    e['numero'], e['bairro'], e['cidade'], e['estado'],
                    e['pais'], e['cep'], c)

        if len(telefones):
            for tel in telefones:
                if tel['tipo'] in self._tiposTelefone:
                    t = self._tiposTelefone[tel['tipo']]
                else:
                    raise Exception('O tipo de telefone \'{0}\' não foi '\
                        'encontrado'.format(tel['tipo']))

                contato.setTelefone(tel['ddd'], tel['prefixo'], tel['sulfixo'],
                    tel['ramal'], t)

        n_id = self._defineIdCadastro()
        self._cadastro[n_id] = contato

    def upgContato(self, id, nome, apelido, site):
        '''
            Método para atualizar os dados de um contato.
        '''
        pass

    def rmContato(self, idContato):
        '''
            Método para remover um contato.
        '''
        pass

    def getContatosResumidos(self):
        '''
            Método para buscar todos os contatos de forma resumida, isto é,
            sem endereço(s) e telefone(s).
        '''
        pass

    def getContato(self, id):
        '''
            Método para buscar um contato.
        '''
        pass

    def upgTelefoneContato(self, idContato, telefone=None):
        '''
            Método para atualizar os dados de um telefone de um contato.

            O argumento "telefone" deve ser informado como um dict contendo as
            seguintes chaves: id, ddd, prefixo, sulfixo, ramal, tipo.
                Ex.: telefone={'id':1, 'ddd':'38', 'prefixo':'3629',
                        'sulfixo':'4600', 'ramal':'', 'tipo':1}
        '''
        pass

    def rmTelefoneContato(self, idContato, idTelefone):
        '''
            Método para remover um telefone de um contato.
        '''
        pass

    def getTelefonesContato(self, idContato):
        '''
            Método para buscar o(s) telefone(s) de um contato.
        '''
        pass

    def upgEnderecoContato(self, idContato, endereco=None):
        '''
            Método para atualizar os dados de um endereço de um contato.

            O argumento "endereço" deve ser informado como um dict contendo as
            seguintes chaves: id, logradouro, complemento, numero, bairro, cidade,
            estado, pais, cep e categoria.
                Ex.: endereco={'id':1, 'logradouro':'Rua ...', 'complemento': '...',
                    'numero':'...', 'bairro':'...', 'cidade':'...',
                    'estado':'...', 'pais':'Brasil', 'cep':'39480-xxx',
                    'categoria':1}
        '''
        pass

    def rmEnderecoContato(self, idContato, idEndereco):
        '''
            Método para remover um endereço de um contato.
        '''
        pass

    def getEnderecoContato(self, idEndereco):
        '''
            Método para buscar o(s) endereço(s) de um contato.
        '''
        pass

    def __repr__(self):
        return '<Agenda1 categoriasEndereco=%s, tiposTelefone=%s, '\
            'cadastro=%s>' % (self._categoriasEndereco, self._tiposTelefone,
            self._cadastro)

if __name__ == '__main__':

    minha_agenda = Agenda1()

    for c in ['Residencial', 'Comercial', 'Veraneio']:
        minha_agenda.addCategoriaEndereco(c)

    for t in ['Celular', 'Comercial', 'Fixo']:
        minha_agenda.addTipoTelefone(t)

    # print(minha_agenda.getCategoriasEndereco())
    # print(minha_agenda.getTiposTelefone())

    c1 = minha_agenda.getCategoriasEndereco()[1][0]
    c2 = minha_agenda.getCategoriasEndereco()[0][0]
    # print(c1)
    # print(c2)
    #
    # print(minha_agenda.getTiposTelefone())

    t1 = minha_agenda.getTiposTelefone()[1][0]
    t2 = minha_agenda.getTiposTelefone()[1][0]
    # print(t1)
    # print(t2)

    minha_agenda.addContato('Danilo Nunes', 'Dan', 'apoena.net.br',
        enderecos=[{'logradouro':'Rua A', 'complemento':'', 'numero':'10',
            'bairro':'Centro', 'cidade':'Ifnmglândia', 'estado':'Cansaço',
            'pais':'Brasil', 'cep':'00000-000', 'categoria':c1},
            {'logradouro':'Rua X', 'complemento':'Barraco', 'numero':'245A',
                'bairro':'Centro', 'cidade':'Ifnmglândia', 'estado':'Cansaço',
                'pais':'Brasil', 'cep':'00000-000', 'categoria':c2}],
        telefones=[{'ddd':'38', 'prefixo':'3629', 'sulfixo':'4600',
            'ramal':'', 'tipo':t1}, {'ddd':'38', 'prefixo':'3629',
            'sulfixo':'4600', 'ramal':'123', 'tipo':t2}])

    print(minha_agenda)
