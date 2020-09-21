Name:       libsysperf
Summary:    Static helper library for CVS and proc file handling
Version:    0.2.4.3
Release:    1
License:    GPLv2
URL:        https://github.com/mer-tools/libsysperf
Source0:    %{name}-%{version}.tar.gz
Requires:   python3-base
BuildRequires:  python3-base

%description
Static helper library for CSV and /proc/ file handling, used by some sp-* tools

%package devel
Summary:    Header files for libsysperf
Requires:   %{name} = %{version}-%{release}
Requires:   %{name} = %{version}

%description devel
Header files needed to build against libsysperf

%prep
%setup -q -n %{name}-%{version}

%build
# build gets done with make install

%install
make install DESTDIR=%{buildroot} LIB=%{_libdir}

%files
%defattr(-,root,root,-)
%{_bindir}/sp_fix_tool_vers
%{_bindir}/sp_gen_changelog
%{_bindir}/sp_gen_manfile
%{_bindir}/sp_textconv
%{_libdir}/libsysperf.a
%{_mandir}/man1/sp_fix_tool_vers.1.gz
%{_mandir}/man1/sp_gen_changelog.1.gz
%{_mandir}/man1/sp_gen_manfile.1.gz
%{_mandir}/man1/sp_textconv.1.gz

%files devel
%defattr(-,root,root,-)
%{_includedir}/libsysperf/argvec.h
%{_includedir}/libsysperf/array.h
%{_includedir}/libsysperf/calculator.h
%{_includedir}/libsysperf/cstring.h
%{_includedir}/libsysperf/csv_calc.h
%{_includedir}/libsysperf/csv_float.h
%{_includedir}/libsysperf/csv_table.h
%{_includedir}/libsysperf/hash.h
%{_includedir}/libsysperf/mem_pool.h
%{_includedir}/libsysperf/msg.h
%{_includedir}/libsysperf/proc_maps.h
%{_includedir}/libsysperf/proc_meminfo.h
%{_includedir}/libsysperf/proc_stat.h
%{_includedir}/libsysperf/proc_statm.h
%{_includedir}/libsysperf/proc_status.h
%{_includedir}/libsysperf/reader.h
%{_includedir}/libsysperf/release.h
%{_includedir}/libsysperf/str_array.h
%{_includedir}/libsysperf/str_pool.h
%{_includedir}/libsysperf/writer.h
%{_includedir}/libsysperf/xmalloc.h
%doc COPYING

