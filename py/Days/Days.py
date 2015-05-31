# coding: utf-8

PHASE_NOT_STARTED = 0 # 始まる前
PHASE_START = 1       # 4.2.1. 開始フェーズ
PHASE_CONVERSATE = 2  # 4.2.2. 会話フェーズ
PHASE_SELECT = 3      # 4.2.3. 対象指定フェーズ
PHASE_EXECUTE = 4     # 4.2.4. 実行フェーズ
PHASE_FINISH = 5      # 4.2.5. 終了フェーズ
PHASE_FINISHED = 6    # 終わった後

# Days is a list of Day
class Days:
    def __init__(self,):
        return
    def start(self,):
        return
    def is_finished(self,):
        return
    def notify(self,):
        return
    def main(self,):
        self.start()
        day_num = 0
        while self.is_finished() == False:
            d = Day(day_num)
            d.main()
            day_num += 1
        self.notify()
        return

# Day is a list of Phase
class Day:
    def __init__(self, day_num):
        self._day_num = day_num
        self._phase = PHASE_NOT_STARTED
        return
    def is_finished(self,):
        return self._phase == PHASE_FINISHED
    def main(self,):
        while self.is_finished() == False:
            p = Phase(self_phase)
            p.main()
            self._phase += 1
        return

class Phase:
    def __init__(self, day_num, phase):
        self._day_num = day_num
        self._phase = phase
        return
    def _start(self,):
        return
    def _conversate(self,):
        return
    def _select(self,):
        if self._day_num == 0:
            return
        else:
            return
        return
    def _execute(self,):
        if self._day_num == 0:
            return
        else:
            return
    def _finish(self,):
        return
    def main(self,):
        if self._phase == PHASE_START:
            self._start()
            return
        if self._phase == PHASE_CONVERSATE:
            self._conversate()
            return
        if self._phase == PHASE_SELECT:
            self._select()
            return
        if self._phase == PHASE_EXECUTE:
            self._execute()
            return
        if self._phase == PHASE_FINISH:
            self._finish()
            return
