import notifier from "src/service/notifier"

export default function uploadFileRejected() {
  notifier('Maximum file size 2Mb')
}
