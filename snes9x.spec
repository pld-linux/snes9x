Summary:	Super NES emulator
Summary(pl):	Emulator Super NES
Name:		snes9x
Version:	1.42
Release:	2
Group:		Applications/Emulators
License:	BSD-style
Source0:	http://www.lysator.liu.se/%{name}/%{version}/%{name}-%{version}-src.tar.gz
# Source0-md5:	1e8af4c590e35352ddac58d25a468676
Patch0:		%{name}-no_nsl.patch
Patch1:		%{name}-system_zlib.patch
URL:		http://www.snes9x.com/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
%ifarch %{ix86}
BuildRequires:	nasm
%endif
BuildRequires:	zlib-devel
Provides:	snes9x-X
Provides:	snes9x-binary
Provides:	snes9x-common
Obsoletes:	snes9x-X
Obsoletes:	snes9x-common
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fomit-frame-pointer

%description
Snes9X is a portable, freeware Super Nintendo Entertainment System
(SNES) emulator. It basically allows you to play most games designed
for the SNES and Super Famicom Nintendo game systems on your PC or
Workstation.

%description
Snes9X jest przeno¶nym, darmowym emulatorem Super Nintendo
Entertainment System (SNES). Zasadniczo pozwala graæ w wiêkszo¶æ gier
przeznaczonych dla SNES i systemów gier Super Famicom Nintendo na PC
lub stacji roboczej.

%prep
%setup -q -n %{name}-%{version}-src
%patch0 -p0
%patch1 -p0

%build
cd %{name}
cp -f /usr/share/automake/config.sub .
%{__aclocal}
%{__autoconf}
%configure
%{__make} \
	OPTIMISE="%{rpmcflags} -fno-exceptions -Wall -W -Wno-unused-parameter -pedantic -pipe"

%install
rm -rf $RPM_BUILD_ROOT
install -D %{name}/%{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -r $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {faqs,license,readme,snes9x/{changes,problems}}.txt readme.unix
%attr(755,root,root) %{_bindir}/%{name}
