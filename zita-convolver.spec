Summary:	C++ library implementing a real-time convolution matrix
Name:		zita-convolver
Version:	4.0.0
Release:	1
License:	GPL v3+
Group:		Libraries
Source0:	http://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	59a86a7901dfab3803003fee090793ab
URL:		http://kokkinizita.linuxaudio.org/linuxaudio/
BuildRequires:	fftw3-single-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C++ library implementing a real-time convolution matrix.

%package devel
Summary:	Header files for %{name} library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{name} library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki %{name}.

%prep
%setup -q

%build
%{__make} -C libs -f Makefile-linux \
	CXXFLAGS="%{rpmcxxflags}" \
	CPPFLAGS="%{rpmcppflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}

cp -p libs/lib%{name}.so.4.* $RPM_BUILD_ROOT%{_libdir}
/sbin/ldconfig -nN $RPM_BUILD_ROOT%{_libdir}
ln -s "$(basename libs/lib%{name}.so.4.*)" $RPM_BUILD_ROOT%{_libdir}/lib%{name}.so
cp -p libs/%{name}.h $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/lib%{name}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/lib%{name}.so.4

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib%{name}.so
%{_includedir}/%{name}.h
