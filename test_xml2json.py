if __name__ == '__main__':
  import nose2

  class Hello(object):
      def startTestRun(self, event):
          print("hello!")

  nose2.discover(extraHooks=[('startTestRun', Hello())])