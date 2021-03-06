class Participant:
    def run(self):
        self.log.info('INIT')
        msg = self.chan.recvFrom(coordinator, TIMEOUT)
        if (not msg): #crashed coordinator - give up entirely
            decision = LOCAL_ABORT
        else:   #coordinator have sent VOTE_REQUEST
            decision = self.do_work()
            if decision == LOCAL_ABORT:
                self.chan.sendTo(coordinator, VOTE_ABORT)
            else:   #ready to commit enter READY state
                self.log.info('READY')
                self.chan.sendTo(coordinator, VOTE_COMMIT)
                msg = self.chan.recvFrom(coordinator, TIMEOUT)
                if (not msg): # crashed cooerdinator - check the others
                    self.chan.sendTo(all_participants, NEED_DECISION)
                    while True:
                        msg = self.chan.recvFromAny()
                        if msg[1] in [GLOBAL_COMMIT, GLOBAL_ABORT, LOCAL_ABORT]:
                            decision = msg[1]
                            break
                else:   #coordinator came to decision
                    decision = msg[1]
            if decision == GLOBAL_COMMIT:
                self.log.info('COMMIT')
            else: #decision in [GLOBAL_ABORT, LOCAL_ABORT]
                self.log.info('ABORT')
            while True: #Help any other participant when  coordinator crashed
                msg = self.chan.recvFrom(all_participants)
                if msg[1] == NEED_DECISION:
                    self.chan.sendTo([msg[0]], decision)

                
