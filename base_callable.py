class MiniCallableDefault(ABC) :
  """
  小規模な関数を作成するためのフォーマットを示すクラス
  非推奨：テストで外部のデータを必要とする処理、テストに時間がかかりすぎる処理

  設計思想
    ・クラスを利用する際に必要な知識を最小にすること

  設計方法
    ・クラスの中にテストを同梱する。
    ->__init__で_testを実行する。
    ->エラーは_testでraiseする。
    ・パブリックメソッドの所持を禁止
    ->一つのCallableDefaultの派生クラスは、外部からの呼び出しを__call__でのみ行う。
    ->持つのは、__call__, __init__とプライベートメンバー("_"始まり)
    ・__call__では変数のdefault値を設定して、_mainを呼び出す(dict.set_default)


  命名方法
    普通のクラスとは異なり、CamelCaseの名詞ではなくCamelCaseの動詞で命名
    -> 例：MinimalCloserではなくMinimalClose
  """

  @abstractmethod
  def __init__(self):
    """
    _testを呼び出して実行する。
    """


  @abstractmethod
  def __call__(self, **kwargs) :
    """
    _set_defaultでデフォルト値を設定し、_mainを呼び出す。
    """



  @abstractmethod
  def _set_default(self, kwargs:dict):
    """
    推奨：dict.set_default
    デフォルトを設定した辞書を返す。
    """


  @abstractmethod
  def _test(self):
    """
    _mainをテストする。
    必要に応じて、__call__も通したテストを含む。
    レポートはprintを使う
    ->成功ケースをprint
    ->失敗ケースは直接例外をraiseする。
    """

  @abstractmethod
  def _main(self, **kwargs):
    """
    メインの処理
    エラーはそのままraiseして、処理を中断する。
    """
