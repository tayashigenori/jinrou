# coding: utf-8

PHASE_START = 1      # 4.2.1. 開始フェーズ
PHASE_CONVERSATE = 2 # 4.2.2. 会話フェーズ
PHASE_SELECT = 3     # 4.2.3. 対象指定フェーズ
PHASE_EXECUTE = 4    # 4.2.4. 実行フェーズ
PHASE_FINISH = 5     # 4.2.5. 終了フェーズ

class Day:
    def __init__(self, day_num):
        self._day_num = day_num
        return
    def process(self,):
        self._start()
        self._conversate()
        self._select()
        self._execute()
        self._finish()
    def _start():
        p = Phase(self._day_num, PHASE_START)
        p.process()
        return
    def _conversate():
        p = Phase(self._day_num, PHASE_CONVERSATE)
        p.process()
        return
    def _select():
        p = Phase(self._day_num, PHASE_SELECT)
        p.process()
        return
    def _execute():
        p = Phase(self._day_num, PHASE_EXECUTE)
        p.process()
        return
    def _finish():
        p = Phase(self._day_num, PHASE_FINISH)
        p.process()
        return

class Phase:
    def __init__(self, day_num, phase_name):
        self._phase_name = phase_name
        self._day_num = day_num
        return
    def process():
        if self._phase_name == PHASE_START:
            return
        if self._phase_name == PHASE_CONVERSATE:
            return
        if self._phase_name == PHASE_SELECT:
            if self._num == 0:
                return
            else:
                return
        if self._phase_name == PHASE_EXECUTE:
            if self._num == 0:
                return
            else:
                return
        if self._phase_name == PHASE_FINISH:
            return
