Name:           odroid-u-base
Version:        0.1.0
Release:        1%{?dist}
Summary:        Basic system configurations for ODROID-X2/U2/U3

Group:          System Environment/Base
License:        BSD
URL:            http://odroid.com/dokuwiki/doku.php?id=en:odroid-u3
Source0:        60-hk_cec.rules
Source1:        Built-in_Audio.conf

BuildArch:      noarch

Requires:       linux-firmware
Requires:       udev

%description
Basic system configurations for ODROID-X2/U2/U3, such as firmware scripts and
rules for udev.

%prep

%build

%install
install -p -m0644 -D %{SOURCE0} %{buildroot}%{_prefix}/lib/udev/rules.d/60-hk_cec.rules
install -p -m0644 -D %{SOURCE1} %{buildroot}%{_datadir}/alsa/cards/Built-in_Audio.conf

install -d %{buildroot}%{_prefix}/lib/firmware/s5p-mfc/
ln -s ../s5p-mfc.fw %{buildroot}%{_prefix}/lib/firmware/s5p-mfc/s5p-mfc.fw
ln -s ../s5p-mfc-v6.fw %{buildroot}%{_prefix}/lib/firmware/s5p-mfc/s5p-mfc-v6.fw

%files
%{_prefix}/lib/udev/rules.d/60-hk_cec.rules
%{_prefix}/lib/firmware/s5p-mfc/
%{_datadir}/alsa/cards/Built-in_Audio.conf
%dir %{_datadir}/alsa
%dir %{_datadir}/alsa/cards

%changelog
* Sun Aug 09 2015 Scott K Logan <logans@cottsay.net> - 0.1.0-1
- Initial package
