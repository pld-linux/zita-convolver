Summary:	C++ library implementing a real-time convolution matrix
Summary(pl.UTF-8):	Biblioteka C++ implementująca macierz konwolucji czasu rzeczywistego
Name:		zita-convolver
Version:	4.0.3
Release:	1
License:	GPL v3+
Group:		Libraries
Source0:	http://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	a357f6ff8588eb53af5335968cfacf3a
URL:		http://kokkinizita.linuxaudio.org/linuxaudio/
BuildRequires:	fftw3-single-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C++ library implementing a real-time convolution matrix.

%description -l pl.UTF-8
Biblioteka C++ implementująca macierz konwolucji czasu rzeczywistego.

%package devel
Summary:	Header files for %{name} library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	fftw3-single-devel
Requires:	libstdc++-devel

%description devel
Header files for %{name} library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki %{name}.

%prep
%setup -q

%build
%{__make} -C source \
	CXXFLAGS="%{rpmcxxflags}" \
	CPPFLAGS="%{rpmcppflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}

cp -p source/lib%{name}.so.4.* $RPM_BUILD_ROOT%{_libdir}
/sbin/ldconfig -nN $RPM_BUILD_ROOT%{_libdir}
ln -s "$(basename $RPM_BUILD_ROOT%{_libdir}/lib%{name}.so.4.*)" $RPM_BUILD_ROOT%{_libdir}/lib%{name}.so
cp -p source/%{name}.h $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/libzita-convolver.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libzita-convolver.so.4

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libzita-convolver.so
%{_includedir}/zita-convolver.h
