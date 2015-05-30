# coding: utf-8

class Day:
    PHASE_INIT = 0       # 始まる前
    PHASE_START = 1      # 4.2.1. 開始フェーズ
    PHASE_CONVERSATE = 2 # 4.2.2. 会話フェーズ
    PHASE_SELECT = 3     # 4.2.3. 対象指定フェーズ
    PHASE_EXECUTE = 4    # 4.2.4. 実行フェーズ
    PHASE_FINISH = 5     # 4.2.5. 終了フェーズ

    def __init__(self, day_num):
        self._day_num = day_num
        self._phase = PHASE_INIT
        return
    def increment_phase(self,):
        self._phase += 1
        return
    def _start(self,):
        return
    def _conversate(self,):
        return
    def _select(self,):
        return
    def _execute(self,):
        return
    def _finish(self,):
        return
    def main(self,):
        if self._phase == PHASE_START:
            return
        if self._phase == PHASE_CONVERSATE:
            return
        if self._phase == PHASE_SELECT:
            if self._day_num == 0:
                return
            else:
                return
        if self._phase == PHASE_EXECUTE:
            if self._day_num == 0:
                return
            else:
                return
        if self._phase == PHASE_FINISH:
            return
