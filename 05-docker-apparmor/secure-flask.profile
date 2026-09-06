#include <tunables/global>
profile secure-flask flags=(attach_disconnected,mediate_deleted) {
  #include <abstractions/base>
  network inet stream,
  network inet6 stream,
  /usr/local/bin/python* ix,
  /usr/local/lib/python*/** r,
  /usr/lib/** r,
  /lib/** r,
  /app/** r,
  /tmp/** rw,
  deny /etc/shadow r,
  deny /root/** rwklx,
}
